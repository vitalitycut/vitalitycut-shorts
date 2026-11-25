# Channel strategy

The performance review task rewrites this file every 3 days from real YouTube numbers in Metricool. The daily autopilot reads it before picking topics.

_Last updated: 2026-11-25. Data: 42 Shorts published Oct 23–Nov 8 08:00; **nothing published since** (17 days; Metricool limit; the 10-video backlog in `videos/` is still unposted and nothing is scheduled in Metricool for Nov 25–Dec 10). Channel totals through Nov 21: **2,434 views total** (+7 since the last review: Nov 19 **3**, Nov 20 **3**, Nov 21 **1**; Nov 18 and Nov 22–24 not reported yet). **Subscribers: 2** (unchanged since Nov 17). Metricool still returns **no per-video rows** (5th review in a row), so no video can be ranked and every pattern below is tentative._

_Monetization (YPP): 2 / 1,000 subs (0.2%) and 2,434 / 10M Shorts views in 90 days (0.024%; 0.012% of the 20M bar from Feb 1, 2027). Fan-funding tier: 2 / 500 subs (0.4%), 2,434 / 3M views (0.08%). At the current 1–3 views/day neither is reachable; posting has to restart first._

## ⛔ Posting is blocked: Metricool's monthly limit
Both months, exactly **20 posts** went out through Metricool before the errors began (Oct 24–31, then Nov 1–Nov 8 08:00). Every post after that returned "You have reached your Metricool account limit." The 20-a-month cap is inferred from the post log, not confirmed with Metricool.

**This is still the only thing that matters.** With no uploads for 17 days the channel has fallen from ~184 views/day (3-upload days) to **1–3 views/day** (Nov 19–21: 3, 3, 1). The back catalogue is close to zero. **Dec 1 is 6 days away**; hand-uploading the backlog is still the only way to get views before then.

Until the owner upgrades the plan, or writes "Metricool limit raised" at the top of this file:
- **Don't schedule anything in Metricool before Dec 1.** Every post will fail.
- **10 finished videos are waiting** in `videos/`. While 10+ are unposted and none have been uploaded, **make no new video that day** (research and add a voiceover script instead).
- **From Dec 1, if there's still no upgrade: schedule 1 a day at 12:00 ET** (20 posts last to Dec 20). Each run schedules **only that day's post** (not the whole month at once), so a failure shows up the same day. Use this order, chosen so length and format alternate (no two consecutive within 3s):
  1. Dec 1 `2026-11-15-coffee-gut-motility` (33s, what-happens-when, food staple)
  2. Dec 2 `2026-11-09-four-minute-strength` (22s, 6 beats)
  3. Dec 3 `2026-11-13-oatmeal-cholesterol-myth` (34s, myth-vs-fact, food staple)
  4. Dec 4 `2026-11-08-lonely-sleep-waves` (24s, 6 beats)
  5. Dec 5 `2026-11-14-eggs-brain-alzheimers` (32s, quick-explainer, food staple)
  6. Dec 6 `2026-11-08-modern-life-gut` (29s)
  7. Dec 7 `2026-11-12-bones-walking-vs-sport` (33s, x-vs-y)
  8. Dec 8 `2026-11-10-night-shift-body-clock` (32s)
  Drop the stale AHA-abstract ones (`energy-drink-reports`, `bp-night-dip-wearable`). From **Dec 9**, post new series videos (one made the day before), still 1 a day at 12:00 ET.
- Once the backlog drops under 10 (Dec 1 onward), go back to making **1 new video a day**, so a fresh one is ready when the backlog runs out.
- After scheduling, always check each post's status with `getScheduledPosts` and put any `ERROR` at the top of the run summary.

## Series (owner request, Nov 18; keep this section in every rewrite)
Every new video belongs to one of 6 named series (Myth or Fact, Food on Trial, Body Clock, Stronger for Longer, Her Health, Hype Check); rules in `PIPELINE.md` step 5b, channel copy in `CHANNEL.md`. When per-video data arrives, compare views and subscribers by series.

## What's working
No per-video data yet (Metricool's YouTube video list returns empty, and its video-count metric stops at Oct 25). Channel daily views (Metricool YTEV02), grouped by how many Shorts went up that day:

| Uploads that day | Days | Avg channel views/day | Per upload |
|---|---|---|---|
| 0 (Nov 9–21, Nov 18 missing) | 12 | 5 (17, 5, 6, 4, 5, 1, 2, 1, 11, 3, 3, 1) | — |
| 1 (Nov 6, Nov 8) | 2 | 68 (23 and 112) | 68 |
| 2 (Oct 24–26, Oct 31) | 4 | 97 | 48 |
| 3 (Oct 27–30, Nov 1–5, Nov 7) | 10 | 184 | 61 |

- **Fresh uploads drive almost all views.** Zero-upload days fell from 17 (Nov 9) to 1–3 (Nov 19–21). Each new Short is worth ~50–70 views on its first day and almost nothing after; the 42-Short catalogue now adds ~2 views/day in total.
- **3 a day didn't lower views per upload** (61 vs 48 at 2 a day, 68 at 1 a day). No case for going back to 2: **keep 3 a day as the target** once posting works again. While capped at 20 posts a month, 1 a day spreads them out with the same views per upload.
- **The 3 best days (Nov 2: 346, Nov 7: 307, Nov 1: 269) all had everyday food/drink staples** (olive oil before carbs; peanuts → brain; coffee vs decaf → dementia, full-fat dairy myth). Heart/BP-heavy days (Nov 3–5) averaged 151. Only 3 days, no per-video split: **still only a lead.**
- **Weakest single-upload day:** stats-first hook "8,200 adults. 24 years. 3 brain takeaways." (Nov 6, 08:00): 23 views all day vs 112 for "Same workout every week? Read this." (Nov 8, 08:00). One comparison only.
- **Subscribers: 2**, both gained Nov 17 from the back catalogue. Too few to credit any CTA or series.
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
Last 5 scripts (Nov 10–15, no new scripts since; 0 new in the 10 days to Nov 25): what-happens-when ×2, x-vs-y, myth-vs-fact, quick-explainer. **All 5 are 32–34 seconds with 7–8 beats**: length has stopped varying. None has a `series` field yet (added to the pipeline Nov 18). Nothing over 37s or under 28s since Nov 1.
- Keep the `"format"` and `"series"` fields on every script.
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

## Experiments queue (Nov 26–28, then the Dec 1 restart)
Nothing can be scored until videos post. Nov 26–30: no new videos, no Metricool scheduling (see the blocked section).
1. **Restart test (Dec 1–3):** coffee-gut (33s) → four-minute-strength (22s) → oatmeal myth (34s), 1 a day at 12:00 ET. Compare each day's channel views to the 1-upload baseline (23 and 112) and the 0-upload floor (now ~2). If a day comes in under 20, the upload probably failed: check `getScheduledPosts`.
2. **Length test (carried over 5 reviews, now built into the Dec order):** 22–24s Shorts (Dec 2, Dec 4) vs 32–34s (Dec 1, 3, 5), by next-day channel views. Needs per-video data to be conclusive.
3. **First series video + hook variety (from Dec 8, made Dec 8 for Dec 9):** a **Myth or Fact** or **Food on Trial** episode with a bold-claim hook, no "If you" and no "read this" (e.g. "Bread isn't the problem."). Compare its first-day channel views with the backlog uploads, and watch subscribers.

**Owner action needed (raised in every review since Nov 10):** (a) reconnect the YouTube account in Metricool (per-video sync looks stopped since ~Oct 25) so videos can be ranked; (b) either raise the Metricool plan or hand-upload the backlog now: each idle day costs ~60–180 views; (c) recording any script in `VOICE_SCRIPTS.md` into `voice/` is still the biggest unused anti-template safeguard.
