# Channel strategy

The performance review task rewrites this file every 3 days from real YouTube numbers in Metricool. The daily autopilot reads it before picking topics.

_Last updated: 2026-11-01. Data: 22 Shorts published (Oct 23–31), 1 failed to post (Oct 31 18:00, "You have reached your Metricool account limit"), 1 pending (today 08:00 ET). Metricool now returns **no per-video rows at all** (9 days in; the 3 rows it used to list are gone too). Channel totals run through Oct 28: **540 views total** (Oct 23: 9, Oct 24: 91, Oct 25: 87, Oct 26: 140, Oct 27: 72, Oct 28: 141), **0 subscribers**, nothing reported for Oct 29–31. No video can be ranked, so nothing below is a proven pattern._

## ⚠ Posting is at risk: Metricool account limit
The Oct 31 18:00 Short ("If you're gaining an hour tonight, read this") **did not publish**. Metricool shows `status: ERROR`, "You have reached your Metricool account limit." Every earlier post published fine. Until the owner fixes this (upgrade the plan or check what limit was hit):
- After scheduling, the autopilot must check each new post's status with `getScheduledPosts` and report any `ERROR` at the top of its summary.
- Don't re-post time-bound videos late (the clock-change Short is now out of date and should stay unposted).
- If the limit turns out to be a monthly post cap, dropping to 2 a day is the fix (see Format mix).

## What's working
Still unproven. The only real numbers are channel-level daily views:

| Day | Shorts live by end of day | Channel views that day | Views per live Short |
|---|---|---|---|
| Oct 23 | 1 | 9 | 9 |
| Oct 24 | 3 | 91 | 30 |
| Oct 25 | 5 | 87 | 17 |
| Oct 26 | 7 | 140 | 20 |
| Oct 27 | 10 (first 3-a-day day) | 72 | 7 |
| Oct 28 | 13 | 141 (best day so far, tied) | 11 |
| Oct 29–31 | 16 → 22 | not reported yet | — |

Daily views have stayed flat at ~70–140 since Oct 24 while the number of live Shorts quadrupled, and no subscriber has been gained. So the back catalogue isn't compounding yet: each new Short adds little. Views per live Short fell from ~20 (2 a day) to ~7–11 (3 a day), but that is expected as the catalogue grows and the 2-a-day vs 3-a-day comparison can't be read without per-video views. **Not a clear enough drop to go back to 2 a day.**

What's been published (all PUBLISHED in Metricool unless noted; views not reported for any):

| Video | Published (ET) | Hook type | Format | Length |
|---|---|---|---|---|
| Creatine isn't just for gym bros | Oct 23 (YouTube app) | Statement, "X isn't just for Y" | Quick explainer | 37s, 8 beats |
| Your leggings might be shedding plastic | Oct 24 12:00 | "Your ___" | Explainer + easy wins | 34s, 7 beats |
| Does magnesium actually help you sleep? | Oct 24 18:00 | Question | Myth vs fact | 37s, 8 beats |
| Is lifting once a week enough? | Oct 25 12:00 | Statement | X vs Y | 35s, 7 beats |
| Your coffee packs 40% more calories | Oct 25 18:00 | "Your ___", number | 3 things | 26s, 6 beats |
| 2 years of fish oil: what happened to memory? | Oct 26 12:00 | Question, number | What happens when | 41s, 8 beats |
| Pilates linked to a longer life? The catch | Oct 26 18:00 | Statement | Quick explainer | 28s, 6 beats |
| Two drinks a day isn't so moderate | Oct 27 08:00 | Statement, myth-bust | X vs Y | 34s, 7 beats |
| Your CBN sleep gummy has a catch | Oct 27 12:00 | "Your ___" | Myth vs fact | 39s, 8 beats |
| Which phone user are you? | Oct 27 18:00 | Question / quiz | 3 things | 42s, 8 beats |
| Cardio may rewire your heart's dimmer switch | Oct 28 08:00 | Statement, body part | What happens when | 25s, 6 beats |
| 6.5 points lower BP from wall sits | Oct 28 12:00 | Number-led | Quick explainer | 32s, 7 beats |
| Your gut may hint how fast you age | Oct 28 18:00 | "Your ___", body part | 3 things | 39s, 8 beats |
| Can brainstacking fix brain rot? | Oct 29 08:00 | Question, trend | Myth vs fact | 28s, 6 beats |
| How you drink tea may matter for your heart | Oct 29 12:00 | Statement | X vs Y | 32s, 7 beats |
| 30 sauna minutes: what happens to your blood | Oct 29 18:00 | Number-led | What happens when | 27s, 6 beats |
| Do you nod off during the day? Read this | Oct 30 08:00 | Question, "you" | 3 things | 45s, 8 beats |
| 20g of fiber vs knee pain? | Oct 30 12:00 | Number-led, body part | X vs Y | 35s, 7 beats |
| Your cranberry juice is probably the wrong one | Oct 30 18:00 | "Your ___", myth-bust | Myth vs fact | 27s, 6 beats |
| Are sugar-free sweets kinder to your brain? | Oct 31 08:00 | Question | Quick explainer | 40s, 8 beats |
| 8 glasses of water a day was never science | Oct 31 12:00 | Statement, myth-bust, number (evergreen) | Myth vs fact | 35s, 8 beats |
| If you're gaining an hour tonight, read this | Oct 31 18:00 — **FAILED (account limit)** | "If you ___" | Explainer + easy wins | 22s, 6 beats |
| You're picturing muscle aging wrong | Nov 1 08:00 (pending) | "You're ___ wrong", body part | Quick explainer | 36s, 8 beats |

Last queue's experiments: (1) evergreen vs news ran (8 glasses of water, Oct 31 12:00); (2) shortest-yet 22s and (3a) "If you" hook at 18:00 were both put on the clock-change Short, which failed to post, so **neither was tested**; (3b) "You're ___ wrong" at 08:00 is going out today.

Test grid so far (live videos): length 22–28s (6) / 32–37s (10) / 39–45s (6); hook question (6) vs statement (16), "Your ___" (5), number-led (6); slot 08:00 (6 incl. today), 12:00 (8), 18:00 (7); 2/day (6 videos) vs 3/day (16).

## Do more of
No proven winners yet, so keep the starting guidance and keep the grid balanced:
- Topics tied to a fresh study or headline, in broad-appeal areas: supplements people already buy, sleep, everyday food and drink, time-saving fitness, brain/phone habits. Mix in evergreen myth-busts (1 every 2–3 days) so the news-vs-evergreen test has more than one data point.
- Hooks of 8 words or fewer that challenge a belief, name a number, or name something the viewer owns, eats or does.
- The "Reality check" beat in every video.
- Subscriber pull: 540 views and 0 subscribers means nothing is asking strongly enough. Make the last beat a specific reason to follow ("Follow for one myth a day, checked against the studies"), and vary that line every video.

## Do less of
- Don't change channel direction on no data. No topic area is "banned" for performance reasons yet.
- Don't stack two experiments on one video (the 22s + "If you" test was lost in one failed post and couldn't have been separated anyway).
- Don't schedule time-bound topics (holidays, clock changes) in the last slot before the event; put them in the first slot so a failure can still be noticed and fixed.
- Keep "Your ___" hooks rare (5 so far); use "Do you…", "If you…", "You're ___" instead.
- Don't repeat a format within the same day.

## Format mix
Used so far: myth vs fact (6), quick explainer (6 incl. today), X vs Y (4), 3 things (4), what happens when (3), explainer + easy wins (2 incl. the failed one). Next 3 days: favor **what happens when**, **X vs Y** and **3 things**; hold myth vs fact and quick explainer to one each. Never the same format twice in one day.

Posting rate: **stay at 3 a day (08:00, 12:00, 18:00)** for now. Channel views per day didn't drop after the move (72 and 141 vs 87 and 140 the days before), so there's no clear harm. Switch to 2 a day (12:00 and 18:00) if either (a) the Metricool account limit is a post cap the owner won't raise, or (b) once per-video views exist, average views at 48h for Oct 27+ Shorts are clearly lower than for Oct 24–26 Shorts.

## Keep it monetizable
Since July 16, 2026, YouTube doesn't monetize repetitive or templated content with little variation between videos ("inauthentic content"). Every video must look and read different from the last one:
- Change the palette, particle style, tag line, label wording and beat structure each time (beat count has been 6–8; keep using all three).
- Vary length between about 22 and 45 seconds.
- Make each one teach something specific; never pad with generic lines.
- Owner voiceover videos (from `voice/`) add a human, non-templated element; use any that are available first. None have been recorded yet, which is the single biggest anti-template safeguard still unused.
- At 3 a day, the risk of looking mass-produced is higher. Same-day videos must differ in format, hook style, palette and tag line. The "The study" / "Reality check" label pair repeats in most videos; vary the middle labels' wording (keep the Reality check beat itself).

## Experiments queue (Nov 2–4)
1. **Shortest yet, re-run:** one ~22s, 6-beat Short in the 18:00 slot with an ordinary statement hook (not "If you"), evergreen or news, to compare against the 25–28s group.
2. **"If you ___" hook, alone:** one 32–37s Short at 12:00 with an "If you ___" hook, so the hook is the only thing that differs from the mid-length 12:00 group.
3. **Follow-reason CTA:** on all Shorts Nov 2–4, end with a specific follow reason (varied wording each time) instead of a plain "Follow for more", and compare subscribers gained Nov 2–4 vs 0 so far.

At the next review, if per-video views are available, compare videos at equal age (views at 48h and views per day since posting) and settle 2 vs 3 a day. If Metricool still lists no per-video rows, ask the owner to check YouTube Studio directly or reconnect YouTube in Metricool.
