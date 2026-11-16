# Channel strategy

The performance review task rewrites this file every 3 days from real YouTube numbers in Metricool. The daily autopilot reads it before picking topics.

_Last updated: 2026-11-16. Data: 42 Shorts published Oct 23–Nov 8 08:00; **nothing has been published since** (Metricool limit; the 5 hand-upload videos from Nov 10–15 haven't gone up). Channel totals through Nov 12: **2,407 views total** (+15 since the last review: Nov 10 **5**, Nov 11 **6**, Nov 12 **4**), **0 subscribers, 0 gained**. Nov 13–15 aren't reported yet. Metricool still returns **no per-video rows**, so no video can be ranked and every pattern below is tentative._

## ⛔ Posting is blocked: Metricool's monthly limit
Both months, exactly **20 posts** went out through Metricool before the errors began (Oct 24–31, then Nov 1–Nov 8 08:00). Every post after that returned "You have reached your Metricool account limit." The 20-a-month cap is inferred from the post log, not confirmed with Metricool.

**This is now the only thing that matters.** With no uploads for 4 days, the channel fell from ~184 views/day (3-upload days) to **4–6 views/day** (Nov 10–12). The 42-Short back catalogue brings in almost nothing; each day without uploads costs ~150–180 views.

Until the owner upgrades the plan, or writes "Metricool limit raised" at the top of this file:
- **Don't schedule anything else in Metricool in November.** Every post will fail.
- Make **at most 1 video a day**, the best candidate. Log it in Clip Desk as `status: "editing"` with "Ready to upload by hand. Metricool monthly limit reached" in `notes`.
- **10 finished videos are waiting** in `videos/`. Upload priority for the owner (newest, evergreen, food-staple first): `2026-11-15-coffee-gut-motility`, `2026-11-14-eggs-brain-alzheimers`, `2026-11-13-oatmeal-cholesterol-myth`, `2026-11-12-bones-walking-vs-sport`, `2026-11-10-night-shift-body-clock`, `2026-11-09-four-minute-strength`, `2026-11-08-modern-life-gut`, `2026-11-08-lonely-sleep-waves`. Drop the stale AHA-abstract ones (`energy-drink-reports`, `bp-night-dip-wearable`).
- If the backlog reaches 10+ unposted videos and none have been uploaded, **make no new video that day** (research and add a voiceover script instead). More unposted videos don't add views.
- From Dec 1, if there's still no upgrade: schedule **1 a day at 12:00 ET**, starting with the backlog above (oldest evergreen first is fine), so the 20 posts last until Dec 20.
- After scheduling, always check each post's status with `getScheduledPosts` and put any `ERROR` at the top of the run summary.

## What's working
No per-video data yet (Metricool's YouTube video list returns empty, and its video-count metric stops at Oct 25). Channel daily views (Metricool YTEV02), grouped by how many Shorts went up that day:

| Uploads that day | Days | Avg channel views/day | Per upload |
|---|---|---|---|
| 0 (Nov 9–12) | 4 | 8 (17, 5, 6, 4) | — |
| 1 (Nov 6, Nov 8) | 2 | 68 (23 and 112) | 68 |
| 2 (Oct 24–26, Oct 31) | 4 | 97 | 48 |
| 3 (Oct 27–30, Nov 1–5, Nov 7) | 10 | 184 | 61 |

- **Fresh uploads drive almost all views.** Zero-upload days dropped from 17 to ~5 views as the last uploads aged. Each new Short is worth ~50–70 views on its first day, and almost nothing after.
- **3 a day didn't lower views per upload** (61 vs 48 at 2 a day). **Keep 3 a day as the target** once posting works again.
- **The 3 best days (Nov 2: 346, Nov 7: 307, Nov 1: 269) all had everyday food/drink staples** (olive oil before carbs; peanuts → brain; coffee vs decaf → dementia, full-fat dairy myth). Heart/BP-heavy days (Nov 3–5) averaged 151. Only 3 days, no per-video split: **still only a lead.**
- **Weakest single-upload day:** stats-first hook "8,200 adults. 24 years. 3 brain takeaways." (Nov 6, 08:00): 23 views all day vs 112 for "Same workout every week? Read this." (Nov 8, 08:00). One comparison only.
- **Subscribers: 0** after ~2,400 views. No CTA wording has produced a subscriber yet.
- **Slot (08:00 / 12:00 / 18:00) can't be compared** without per-video views.

## Do more of
- **Everyday food and drink staples** (coffee, dairy, eggs, oats, bread, olive oil, nuts, tea, fruit): on all 3 best days. About **1 in 3** videos once posting resumes.
- **Personal habit hooks** that name something the viewer does, but rotate the wording (question, "Your ___", "If you ___", a bold claim to bust).
- **Evergreen myth-busts** of food and fitness rules: they stay usable while videos wait days or weeks to be posted.
- **Women's health / midlife** (cycle, perimenopause): about 1 every 2–3 days.
- **Voiceover videos:** the moment any recording appears in `voice/`, it goes first.

## Do less of
- **"If you ___" / "read this" hooks.** "If you ___" opens 3 of the last 5 hooks (night shift, bones, eggs), and "read this" is in 4 of the last 11 hooks/titles (Nov 8 workout, Nov 8 modern life, Nov 10 night shift, Nov 14 eggs). That's becoming a template. **Don't use the phrase "read this" in the next 5 videos.**
- **Stats-first study hooks** ("8,200 adults. 24 years…"). Sample size goes in beat 2 or later.
- **Heart and blood-pressure topics:** at most 1 every 2 days.
- **Mouse/lab-only studies:** at most 1 every 3 days.
- **Short-shelf-life news** (conference abstracts): videos are waiting days to post, so prefer findings that stay true for weeks.
- **Repeated CTA wording:** never reuse a CTA phrase from the last 10 videos.

## Format mix
Last 5 scripts (Nov 10–15): what-happens-when ×2, x-vs-y, myth-vs-fact, quick-explainer. **All 5 are 32–34 seconds with 7–8 beats**: length has stopped varying. Nothing over 37s or under 28s since Nov 1.
- Keep the `"format"` field on every script.
- Next videos: **"3 things"** (unused recently), **myth vs fact**, **X vs Y**. Never repeat a format on consecutive days.
- Length: next 3 videos should be roughly **24s (6 beats)**, **40–45s (8 beats)**, and one in between. No two in a row within 3s of each other.

Posting rate: **3 a day once the Metricool limit is raised.** No evidence that 3 a day hurt views per video; views scale with uploads.

## Keep it monetizable
Since July 16, 2026, YouTube doesn't monetize repetitive or templated content with little variation between videos ("inauthentic content"). Every video must look and read different from the last one:
- Change the palette, particle style, tag line, label wording and beat structure each time (use 6, 7 and 8 beats).
- Vary length between about 22 and 45 seconds. The last 5 were all 32–34s; fix that now.
- Vary the hook pattern. The "If you ___, read this" pattern is close to a template; rest it.
- Make each one teach something specific; never pad with generic lines.
- Don't let one topic area dominate. The food-staple lead must not become a run of near-identical "study says food X linked to Y" videos: alternate myth-busts, how-tos and comparisons, and vary the foods.
- Owner voiceover videos (from `voice/`) add a human, non-templated element; use any that are available first. **None recorded yet.** Still the biggest anti-template safeguard left unused.
- Same-day videos must differ in format, hook style, palette and tag line. Vary the "The study" / middle label wording (keep the Reality check beat itself) and the CTA line.

## Experiments queue (Nov 17–19)
These can only be scored once videos actually post. Until then, carry them over.
1. **Restart test:** when the owner hand-uploads the backlog, upload **1 a day at 12:00 ET** (coffee-gut → eggs → oatmeal). Compare each day's channel views to the 1-upload baseline (23 and 112) and the 0-upload floor (~5).
2. **Hook variety:** the next new video uses a hook with no "If you" and no "read this" (e.g. a bold myth: "Bread isn't the problem."). Compare its first-day channel views with the "If you…" uploads.
3. **Length test (carried over 2 reviews):** one 40–45s, 8-beat practical how-to, and one ~24s, 6-beat Short. Same comparison.

At the next review: if Metricool still returns no per-video rows, **the owner should reconnect the YouTube account in Metricool** (its video sync looks stopped since ~Oct 25), or read per-video views from YouTube Studio. Until then no test can be scored per video.
