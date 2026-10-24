"""Render text-driven vertical Shorts (1080x1920, 30fps) with an original ambient audio bed."""
import json, math, random, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
FONT_DIR = "/usr/share/fonts/opentype/inter/"
F_HEAD = ImageFont.truetype(FONT_DIR + "InterDisplay-ExtraBold.otf", 96)
F_HEAD_S = ImageFont.truetype(FONT_DIR + "InterDisplay-ExtraBold.otf", 80)
F_LABEL = ImageFont.truetype(FONT_DIR + "Inter-Bold.otf", 34)
F_SMALL = ImageFont.truetype(FONT_DIR + "Inter-SemiBold.otf", 38)
F_TAG = ImageFont.truetype(FONT_DIR + "Inter-Bold.otf", 30)
LEFT, MAXW = 90, 880          # stay clear of Shorts' right-side buttons
TEXT_TOP, TEXT_BOTTOM = 470, 1330  # stay clear of the bottom caption/title area


def ease_out(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def parse_words(text):
    """'**word**' marks accent words. Returns list of (word, accent)."""
    out = []
    for raw in text.split():
        acc = raw.startswith("**") or raw.endswith("**")
        out.append((raw.replace("**", ""), acc))
    return out


def wrap(words, font, maxw):
    lines, cur = [], []
    for w in words:
        trial = " ".join(x[0] for x in cur + [w])
        if cur and font.getlength(trial) > maxw:
            lines.append(cur)
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(cur)
    return lines


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def make_line_img(line, font, fg, accent):
    asc, desc = font.getmetrics()
    lh = asc + desc
    width = int(font.getlength(" ".join(w for w, _ in line))) + 8
    img = Image.new("RGBA", (width, lh + 10), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x = 0
    space = font.getlength(" ")
    for w, acc in line:
        d.text((x, 0), w, font=font, fill=accent if acc else fg)
        x += font.getlength(w) + space
    return img


def build_background(cfg):
    top, bot = np.array(hexrgb(cfg["bg_top"]), float), np.array(hexrgb(cfg["bg_bottom"]), float)
    t = np.linspace(0, 1, H)[:, None]
    grad = top * (1 - t) + bot * t
    arr = np.repeat(grad[:, None, :], W, axis=1).reshape(H, W, 3)
    return Image.fromarray(arr.astype(np.uint8), "RGB")


class Particles:
    def __init__(self, cfg, seed):
        rnd = random.Random(seed)
        self.kind = cfg["particles"]
        self.col = hexrgb(cfg["particle"])
        self.items = []
        n = 34 if self.kind == "fibers" else 18
        for _ in range(n):
            self.items.append(dict(
                x=rnd.uniform(0, W), y=rnd.uniform(0, H), vx=rnd.uniform(-8, 8), vy=rnd.uniform(-26, -8),
                r=rnd.uniform(6, 22) if self.kind == "orbs" else rnd.uniform(30, 90),
                a=rnd.uniform(0, math.tau), spin=rnd.uniform(-0.6, 0.6), ph=rnd.uniform(0, math.tau),
                alpha=rnd.uniform(40, 110)))

    def draw(self, layer, t):
        d = ImageDraw.Draw(layer)
        for p in self.items:
            x = (p["x"] + p["vx"] * t + 30 * math.sin(t * 0.4 + p["ph"])) % W
            y = (p["y"] + p["vy"] * t) % H
            a = int(p["alpha"] * (0.6 + 0.4 * math.sin(t * 0.9 + p["ph"])))
            c = self.col + (a,)
            if self.kind == "orbs":
                r = p["r"]
                d.ellipse([x - r, y - r, x + r, y + r], fill=c)
            else:
                ang = p["a"] + p["spin"] * t
                L = p["r"]
                pts = []
                for i in range(7):  # wavy fiber
                    s = (i / 6 - 0.5) * L
                    wob = 6 * math.sin(i * 1.3 + t * 1.5 + p["ph"])
                    pts.append((x + s * math.cos(ang) - wob * math.sin(ang), y + s * math.sin(ang) + wob * math.cos(ang)))
                d.line(pts, fill=c, width=4, joint="curve")


def render(cfg, out_path):
    fg, accent = hexrgb(cfg["fg"]), hexrgb(cfg["accent"])
    muted = hexrgb(cfg["muted"])
    beats = cfg["beats"]
    # timing
    t = 0.0
    for b in beats:
        n = len(b["text"].replace("**", "").split())
        b["dur"] = b.get("dur") or round(1.4 + 0.34 * n, 2)
        b["start"] = t
        t += b["dur"]
    total = t
    frames = int(math.ceil(total * FPS))
    # prebuild text
    for b in beats:
        font = F_HEAD
        lines = wrap(parse_words(b["text"]), font, MAXW)
        if len(lines) > 5:
            font = F_HEAD_S
            lines = wrap(parse_words(b["text"]), font, MAXW)
        b["imgs"] = [make_line_img(l, font, fg, accent) for l in lines]
        asc, desc = font.getmetrics()
        b["lh"] = int((asc + desc) * 1.04)
        block = b["lh"] * len(lines)
        b["y0"] = int(TEXT_TOP + (TEXT_BOTTOM - TEXT_TOP - block) / 2)
    bg = build_background(cfg)
    parts = Particles(cfg, cfg["seed"])
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-i", out_path + ".wav", "-c:v", "libx264", "-preset", "medium",
                           "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest",
                           "-movflags", "+faststart", out_path], stdin=subprocess.PIPE)
    make_audio(out_path + ".wav", total + 0.2, cfg["chord"], [b["start"] for b in beats])
    for fi in range(frames):
        tt = fi / FPS
        frame = bg.copy().convert("RGBA")
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        parts.draw(layer, tt)
        layer = layer.filter(ImageFilter.GaussianBlur(2))
        frame.alpha_composite(layer)
        d = ImageDraw.Draw(frame)
        # progress bar
        d.rounded_rectangle([LEFT, 300, LEFT + MAXW, 308], 4, fill=muted + (90,))
        d.rounded_rectangle([LEFT, 300, LEFT + max(8, int(MAXW * tt / total)), 308], 4, fill=accent + (255,))
        # series tag
        d.text((LEFT, 340), cfg["tag"], font=F_TAG, fill=muted)
        # current beat
        b = next(x for x in reversed(beats) if tt >= x["start"])
        lt = tt - b["start"]
        out_a = 1.0
        is_last = b is beats[-1]
        if not is_last and lt > b["dur"] - 0.25:
            out_a = max(0.0, (b["dur"] - lt) / 0.25)
        # label chip
        if b.get("label"):
            la = ease_out(lt / 0.3) * out_a
            lab = b["label"].upper()
            tw = F_LABEL.getlength(lab)
            chip = Image.new("RGBA", (int(tw) + 44, 64), (0, 0, 0, 0))
            cd = ImageDraw.Draw(chip)
            chip_bg = hexrgb(b.get("label_bg", cfg["accent"]))
            cd.rounded_rectangle([0, 0, chip.width - 1, 63], 32, fill=chip_bg + (255,))
            cd.text((22, 12), lab, font=F_LABEL, fill=hexrgb(cfg["chip_fg"]))
            chip.putalpha(chip.getchannel("A").point(lambda v: int(v * la)))
            frame.alpha_composite(chip, (LEFT, b["y0"] - 110 + int(20 * (1 - ease_out(lt / 0.3)))))
        # lines
        for i, img in enumerate(b["imgs"]):
            p = ease_out((lt - 0.08 - i * 0.11) / 0.42)
            if p <= 0:
                continue
            a = p * out_a
            im = img.copy()
            im.putalpha(im.getchannel("A").point(lambda v, a=a: int(v * a)))
            y = b["y0"] + i * b["lh"] + int(46 * (1 - p)) - int(14 * (1 - out_a))
            frame.alpha_composite(im, (LEFT, y))
        # footnote
        if b.get("note"):
            na = ease_out((lt - 0.5) / 0.4) * out_a
            d.text((LEFT, b["y0"] + len(b["imgs"]) * b["lh"] + 40), b["note"], font=F_SMALL,
                   fill=muted + (int(255 * na),))
        ff.stdin.write(frame.convert("RGB").tobytes())
    ff.stdin.close()
    ff.wait()
    return total


def make_audio(path, dur, chord, hits, sr=44100):
    t = np.arange(int(dur * sr)) / sr
    sig = np.zeros_like(t)
    for i, f in enumerate(chord):
        lfo = 0.55 + 0.45 * np.sin(2 * np.pi * (0.07 + 0.03 * i) * t + i)
        sig += lfo * (np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t + 0.3)) / len(chord)
    # soft pluck on each beat change
    for h in hits:
        n0 = int(h * sr)
        n = int(0.9 * sr)
        if n0 + n > len(t):
            n = len(t) - n0
        tt = np.arange(n) / sr
        env = np.exp(-tt * 5.5)
        sig[n0:n0 + n] += 0.35 * env * np.sin(2 * np.pi * chord[-1] * 2 * tt)
    # gentle lowpass (moving average) and fades
    k = 12
    sig = np.convolve(sig, np.ones(k) / k, mode="same")
    fade = np.minimum(1, np.minimum(t / 1.2, (dur - t) / 1.5))
    sig = sig * np.clip(fade, 0, 1)
    sig = sig / (np.abs(sig).max() + 1e-9) * 0.32
    data = (sig * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(data.tobytes())


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    total = render(cfg, sys.argv[2])
    print(f"{sys.argv[2]}: {total:.1f}s")
