# Channel strategy

The performance review task rewrites this file every 3 days from real YouTube numbers in Metricool. The daily autopilot reads it before picking topics.

_Last updated: 2026-11-10. Data: 41 Shorts published Oct 23–Nov 8, plus **6 failed** with "You have reached your Metricool account limit" (Oct 31 18:00, Nov 8 12:00 and 18:00, and all three Nov 9 slots). Nothing is scheduled for Nov 10 or later. Metricool still returns **no per-video views** (3 rows have titles but no numbers). Channel totals through Nov 6: **1,956 views total** (+1,416 since the last review's Oct 28 cutoff), **0 subscribers, 0 gained**. Nov 6 (23 views) is probably partial, and Nov 7–9 aren't reported yet. No video can be ranked yet, so every pattern below is tentative._

## ⛔ Posting is blocked: Metricool's monthly limit
In **both** months, exactly **20 posts** went out through Metricool before the errors began: Oct 24–31 (20 posts, then the Oct 31 18:00 failure) and Nov 1–Nov 8 08:00 (20 posts, then 5 failures in a row). That looks like a cap of **20 posts a month** on the current Metricool plan. This is an inference from the post log, not confirmed with Metricool. At 3 a day, the cap runs out by about day 7 of each month.

Until the owner upgrades the plan, or writes "Metricool limit raised" at the top of this file:
- **Don't schedule anything else in Metricool in November.** Every post will fail.
- Make **at most 1 video a day**, the best candidate. Log it in Clip Desk as `status: "editing"` with "Ready to upload by hand. Metricool monthly limit reached" in `notes`, so the owner can upload it in the YouTube app (the Oct 23 Short went out that way).
- The 5 failed videos are finished and in `videos/`. The evergreen ones (`2026-11-08-lonely-sleep-waves`, `2026-11-09-four-minute-strength`, `2026-11-08-modern-life-gut`) are still worth posting. The AHA-abstract ones (`energy-drink-reports`, `bp-night-dip-wearable`) are going stale.
- From Dec 1, if there's still no upgrade: schedule **1 a day at 12:00 ET** so the 20 posts last until Dec 20, rather than burning them all in a week.
- After scheduling, always check each post's status with `getScheduledPosts` and put any `ERROR` at the top of the run summary.

## What's working
We still can't say which videos work, because there are no per-video numbers. Channel daily views (Metricool, YTEV02):

| Period | Days | Uploads/day | Channel views | Avg views/day | Views/day per daily upload |
|---|---|---|---|---|---|
| Oct 24–26 | 3 | 2 | 318 | 106 | 53 |
| Oct 27–Nov 5 | 10 | 3 | 1,606 | 161 | 54 |

Daily detail: Oct 27: 72, Oct 28: 141, Oct 29: 138, Oct 30: 118, Oct 31: 69, **Nov 1: 269, Nov 2: 346 (best day)**, Nov 3: 143, Nov 4: 174, Nov 5: 136, Nov 6: 23 (likely partial).

- **3 a day didn't lower views per upload:** 54 channel views/day per daily upload, vs 53 at 2 a day. Total views per day rose about 50%. So on performance alone there's no reason to go back to 2 a day. The Metricool cap is what limits posting now.
- **Nov 1–2 spike (269 and 346, about 2.2x the 3-a-day average).** That was the first stretch of "If you ___" hooks (back pain, "If you only stroll") and the first days of the follow-reason CTA test. Uploads those days: muscle aging (36s), back pain (33s), olive oil before carbs (23s), period → heart risk (37s), brisk vs casual walking (33s), peanuts → brain scans (22s). We can't tell which video drove the spike. One of them probably got picked up, and **it's only a lead, not a pattern.**
- **The catalogue isn't compounding:** views settled back to about 140/day after the spike while live Shorts grew from 24 to 36.
- **Subscribers: still 0** after about 1,950 views, and 20 posted Shorts since Nov 1 ended with a specific follow reason. The CTA test (experiment 3 last time) showed no effect.

## Do more of
- **Body-part and personal "If you ___ / your ___" hooks.** They were live on the best days (Nov 1–2). Keep using them about once a day so per-video data can confirm or reject them once it arrives.
- **Everyday-behavior topics** (walking pace, sleeping in, what you eat or drink, workout habits) over lab or mouse findings. Viewers can act on them, and most Nov 1–2 uploads were like this.
- **Evergreen myth-busts and practical how-tos** (4-minute workout, lonely sleep waves, water, dairy). They stay relevant if a post is delayed, which matters now that posts are capped.
- **Women's health / midlife** (period → heart, menopause): broad audience and little competition. Keep about 1 every 2–3 days.

## Do less of
- **Heart and blood-pressure topics: 8 of the last 25 videos** (women's heart, potassium, sleep schedule → heart, B12 → heart, traffic noise → heart, avocado/mango arteries, energy drinks → cardiac arrest, BP night dip). Most came from the same AHA Scientific Sessions press batch. Cap it at **1 heart/BP video every 2 days**, both for variety (see the monetization rules) and to test other areas.
- **Mouse/lab-only studies** (olive oil in mice, BRP "natural Ozempic", enamel gel, cardiolipin). The honest "only in mice" hedge weakens the payoff. At most 1 every 3 days.
- **Repeated CTA wording.** "minus the hype" / "without the hype" ended 5 videos. Each CTA must be new, and never reuse a phrase from the last 10 videos.
- Don't stack two experiments on one video, and don't put time-bound topics in the last slot before an event.

## Format mix
Nov 1–9 lengths: 22–26s (9 videos) / 28–33s (10) / 34–37s (6). Beats: 6 (9), 7 (7), 8 (9). That's balanced; keep it that way.
Formats used through Oct 31 (from the last review): myth vs fact (6), quick explainer (6), X vs Y (4), 3 things (4), what happens when (3), explainer + easy wins (2). Since scripts don't record their format, **add a `"format"` field to every new script JSON** (e.g. `"format": "x-vs-y"`) so the next review can measure it.
Next videos: favor **X vs Y** and **what happens when** (least used). Never the same format twice in a day.

Posting rate: **3 a day remains the target once the Metricool limit is raised** (no measurable drop in views per upload). Until then, follow the limit rules at the top.

## Keep it monetizable
Since July 16, 2026, YouTube doesn't monetize repetitive or templated content with little variation between videos ("inauthentic content"). Every video must look and read different from the last one:
- Change the palette, particle style, tag line, label wording and beat structure each time (keep using 6, 7 and 8 beats).
- Vary length between about 22 and 45 seconds (nothing over 37s since Nov 1; try one 40–45s).
- Make each one teach something specific; never pad with generic lines.
- Don't let one topic area (currently heart/BP) dominate the feed. A run of near-identical "study says X linked to heart risk" videos is exactly what reviewers flag as low-variation.
- Owner voiceover videos (from `voice/`) add a human, non-templated element; use any that are available first. **None recorded yet.** This is still the biggest anti-template safeguard left unused, and it matters more now that fewer posts go out.
- Same-day videos must differ in format, hook style, palette and tag line. Vary the "The study" / middle label wording (keep the Reality check beat itself) and the CTA line.

## Experiments queue (Nov 11–13)
Only run these if posting works again (limit raised, or the owner uploads by hand). Otherwise carry them over.
1. **Non-heart week:** no heart/BP topics Nov 11–13. Compare channel views/day against the Nov 3–5 heart-heavy days (143, 174, 136 → avg 151).
2. **"If you ___" hook at 08:00 vs the 12:00 group:** one 30–34s "If you ___" Short at 08:00, everyday-behavior topic, so slot is the only change from Nov 2/3's 12:00 "If you" videos.
3. **Long-end test:** one 40–45s, 8-beat practical how-to (no new study needed), to fill the untested long end of the length range.

At the next review: if Metricool still shows no per-video views, the owner should **reconnect YouTube in Metricool** or read per-video views from YouTube Studio. Without them, none of these tests can be scored.
