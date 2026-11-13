# Channel strategy

The performance review task rewrites this file every 3 days from real YouTube numbers in Metricool. The daily autopilot reads it before picking topics.

_Last updated: 2026-11-13. Data: 42 Shorts published Oct 23–Nov 8 (the last Metricool post went out Nov 8 08:00). Since then: 5 Metricool failures (monthly limit), and 2 finished videos (Nov 10, Nov 12) waiting for a hand upload. Channel totals through Nov 9: **2,392 views total** (+436 since the last review: Nov 7 **307**, Nov 8 112, Nov 9 17), **0 subscribers, 0 gained**. Nov 10–12 aren't reported yet. Metricool still returns **no per-video views**, so no video can be ranked and every pattern below is tentative._

## ⛔ Posting is blocked: Metricool's monthly limit
In **both** months, exactly **20 posts** went out through Metricool before the errors began: Oct 24–31 (then the Oct 31 18:00 failure) and Nov 1–Nov 8 08:00 (then 5 failures in a row, Nov 8 12:00 through Nov 9 18:00). That looks like a cap of **20 posts a month** on the current Metricool plan. This is an inference from the post log, not confirmed with Metricool.

**Why this matters more than any topic choice:** daily channel views follow how many Shorts went up that day (table below). The day with 0 uploads (Nov 9) got 17 views; days with 3 uploads averaged 184. Every day without an upload costs roughly 60–170 views.

Until the owner upgrades the plan, or writes "Metricool limit raised" at the top of this file:
- **Don't schedule anything else in Metricool in November.** Every post will fail.
- Make **at most 1 video a day**, the best candidate. Log it in Clip Desk as `status: "editing"` with "Ready to upload by hand. Metricool monthly limit reached" in `notes`, so the owner can upload it in the YouTube app.
- **7 finished videos are waiting** in `videos/`. Upload priority for the owner: `2026-11-10-night-shift-body-clock`, `2026-11-12-bones-walking-vs-sport`, `2026-11-09-four-minute-strength`, `2026-11-08-modern-life-gut`, `2026-11-08-lonely-sleep-waves`. Drop the stale AHA-abstract ones (`energy-drink-reports`, `bp-night-dip-wearable`).
- From Dec 1, if there's still no upgrade: schedule **1 a day at 12:00 ET** so the 20 posts last until Dec 20. Views per upload were about the same at 1, 2 or 3 a day, so spreading them out loses little and avoids dead days.
- After scheduling, always check each post's status with `getScheduledPosts` and put any `ERROR` at the top of the run summary.

## What's working
Per-video numbers are still missing. Metricool's video list only has the first 3 Shorts (Oct 23–24, titles with no views), and its video-count metric stops at Oct 25, so its YouTube video sync looks stuck. Channel daily views (Metricool YTEV02), grouped by how many Shorts went up that day:

| Uploads that day | Days | Avg channel views/day | Per upload |
|---|---|---|---|
| 0 (Nov 9) | 1 | 17 | — |
| 1 (Nov 6, Nov 8) | 2 | 68 (23 and 112) | 68 |
| 2 (Oct 24–26, Oct 31) | 4 | 97 | 48 |
| 3 (Oct 27–30, Nov 1–5, Nov 7) | 10 | 184 | 61 |

- **Fresh uploads drive almost all views.** With about 42 Shorts live, a day with no upload got 17 views. The back catalogue isn't bringing in views; each new Short is worth about 50–70 views on its first day.
- **3 a day didn't lower views per upload** (61 vs 48 at 2 a day). **Keep 3 a day as the target** once posting works again. Don't go back to 2.
- **The 3 best days (Nov 2: 346, Nov 7: 307, Nov 1: 269) all had everyday food/drink staples:** olive oil before carbs and muscle aging (Nov 1); peanuts → brain, brisk walking and period → heart risk (Nov 2); **coffee vs decaf → dementia**, full-fat dairy myth and enamel gel (Nov 7). Heart/BP-heavy days (Nov 3–5) averaged 151. That's 3 days of data with no per-video split, so **it's only a lead.**
- **Two weak 1-upload days, both at 08:00:** "8,200 adults. 24 years. 3 brain takeaways." (Nov 6) got 23 channel views all day, vs 112 for "Same workout every week? Read this." (Nov 8). That's a single comparison, but the stats-first, study-design hook is the weakest one we've seen.
- **Subscribers: still 0** after about 2,400 views. The specific follow-reason CTA hasn't produced one. (Check YouTube Studio once to confirm Metricool's 0 is right.)

## Do more of
- **Everyday food and drink staples people consume daily** (coffee, dairy, eggs, oats, bread, olive oil, nuts, tea, fruit). They were on all 3 best days. Aim for **1 a day** while the limit applies.
- **Personal "If you ___ / your ___" or habit-question hooks** that name something the viewer does ("Same workout every week?", "If you only stroll", "If you sleep in on weekends"). Put the behavior first, not the study.
- **Myth-busts of food and fitness "rules"** (full-fat dairy, 8 glasses of water, cardio vs weights). They're evergreen, which matters while posts are capped and delayed.
- **Women's health / midlife** (period → heart, menopause): about 1 every 2–3 days.

## Do less of
- **Stats-first study hooks** ("8,200 adults. 24 years…", "6.5 points lower BP…"). Put the sample size in a later beat; lead with the viewer's habit or the surprise.
- **Heart and blood-pressure topics:** at most **1 every 2 days** (8 of 25 videos Nov 1–9 were heart/BP, and those days were below average).
- **Mouse/lab-only studies** (enamel gel, BRP "natural Ozempic", cardiolipin): at most 1 every 3 days. Lead with a viewer behavior if you use one.
- **Conference abstracts with a short shelf life** (AHA abstracts went stale while waiting to post). Prefer findings that stay true for weeks.
- **Repeated CTA wording.** Never reuse a CTA phrase from the last 10 videos.

## Format mix
Lengths of the last 15 scripts: 22–25s (5), 26–31s (4), 32–34s (6). Beats: 6 (6), 7 (3), 8 (6). Nothing over 37s since Nov 1, so the long end is still untested.
Only the Nov 10 (`what-happens-when`) and Nov 12 (`x-vs-y`) scripts have a `"format"` field. **Keep adding `"format"` to every script** so formats can be measured once per-video data arrives.
Next videos: rotate **myth vs fact** (fits the food-staple lead), **X vs Y**, and **what happens when**. Never repeat a format on consecutive days while making 1 a day.

Posting rate: **3 a day remains the target once the Metricool limit is raised.** Views scale with uploads, and there was no drop in views per upload at 3 a day.

## Keep it monetizable
Since July 16, 2026, YouTube doesn't monetize repetitive or templated content with little variation between videos ("inauthentic content"). Every video must look and read different from the last one:
- Change the palette, particle style, tag line, label wording and beat structure each time (keep using 6, 7 and 8 beats).
- Vary length between about 22 and 45 seconds (try one 40–45s).
- Make each one teach something specific; never pad with generic lines.
- Don't let one topic area dominate the feed. The food-staple lead must not turn into a run of near-identical "study says food X linked to Y" videos: alternate myth-busts, how-tos and comparisons, and vary the foods.
- Owner voiceover videos (from `voice/`) add a human, non-templated element; use any that are available first. **None recorded yet.** This is still the biggest anti-template safeguard left unused.
- Same-day videos must differ in format, hook style, palette and tag line. Vary the "The study" / middle label wording (keep the Reality check beat itself) and the CTA line.

## Experiments queue (Nov 14–16)
These run only if the videos get posted (owner uploads by hand, or the limit is raised). Otherwise carry them over.
1. **Food-staple myth-bust:** one 28–34s myth vs fact Short on an everyday staple not yet covered (e.g. eggs, oats, bread or fruit juice), with a personal hook ("If you skip ___", "Your morning ___"). Compare its first-day channel views to the 1-upload days (23 and 112).
2. **Hook order:** if a study has a big number, put the viewer's habit in beat 1 and the number in beat 2 or 3. No stats-first hooks this week.
3. **Long-end test (carried over):** one 40–45s, 8-beat practical how-to (no new study needed).

At the next review: if Metricool still shows no per-video views, **the owner needs to reconnect the YouTube account in Metricool** (its video sync appears to have stopped around Oct 25), or read per-video views from YouTube Studio. Until then none of these tests can be scored per video.
