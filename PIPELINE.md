# Daily Shorts pipeline

This is the runbook for the VitalityCut daily Shorts autopilot. Each run makes **2 original wellness Shorts**, hosts them in this repo, and schedules them on the VitalityCut YouTube channel through Metricool.

## Fixed IDs

- GitHub repo: `vitalitycut/vitalitycut-shorts` (public, branch `main`)
- Metricool brand (blogId): `7593557`, timezone `America/New_York`, YouTube is the only network
- Clip Desk tracker: Artifact `https://claude.ai/artifact/1ZuEek9yExB9F97wkEdKnQ`, database collection `clips`

## Steps

1. **Get push access and clone.** Call `add_repo` (owner `vitalitycut`, repo `vitalitycut-shorts`, access `push`), then clone with `git clone --depth 1`. Install nothing else; `ffmpeg`, Python, Pillow and numpy are preinstalled. Fonts: Inter in `/usr/share/fonts/opentype/inter/`.
2. **Check what's already done.** With ArtifactData, `list` the `clips` collection. With Metricool, `getScheduledPosts` for blogId `7593557` covering the next 3 days. Don't repeat a topic made in the last 30 days (look at `scripts/` file names and Clip Desk titles).
3. **Read `STRATEGY.md` first** and follow its current guidance on topics, hooks, formats and length. It's updated every few days from real view counts, so it overrides the defaults below when they differ.
   **Pick 2 topics.** WebSearch what is trending in wellness this week (searches, news, big podcast episodes). Good fits: supplements, sleep, gut health, women's health, longevity, fitness habits, food myths, wellness tech. Skip anything political, weight-loss pressure aimed at teens, or topics where the honest answer is "see a doctor".
4. **Research each topic.** Use at least 2 credible sources per video (peer-reviewed reviews, PMC/NIH, university press releases, major health outlets). Note what's well supported vs. preliminary.
5. **Write the script** as a JSON file in `scripts/YYYY-MM-DD-slug.json`, following the two existing examples:
   - 6–8 beats, 28–40 seconds total. Beat 1 is the hook (≤8 words), and the last beat is the follow CTA.
   - **Always include a "Reality check" beat** (label_bg `#F2C14E`) that states the limits of the evidence.
   - Mark 1–3 accent words per beat with `**word**`.
   - Use a new palette for each video (dark background, one bright accent that passes contrast against it), `particles` either `orbs` or `fibers`, a different `seed`, and a calm 4-note `chord`.
   - Vary the format across days: myth vs. fact, "3 things", "X vs Y", "what happens when", a quick explainer.
6. **Accuracy rules (non-negotiable).** Every claim must come from your sources that day. Hedge preliminary findings ("early studies", "may"). Never claim something cures or treats a disease. Supplement doses are allowed only as "most studied" amounts, with a note to ask a doctor. Nothing aimed at kids.
7. **Render:** `python3 tools/render.py scripts/<file>.json videos/<same-name>.mp4`, about 2–3 minutes each. Then check one frame from each video (extract with ffmpeg and look at it) for clipped or overlapping text. Delete the leftover `.wav` files.
8. **Commit and push** both scripts and videos to `main`. The video URL is `https://raw.githubusercontent.com/vitalitycut/vitalitycut-shorts/main/videos/<file>.mp4`.
9. **Schedule in Metricool** with `createScheduledPost`, one post per video:
   - Slots: **12:00** and **18:00** America/New_York, on the earliest day(s) from today on where that slot is still free and in the future. Aim for no more than 2 posts per day in total.
   - `providers: [{"network":"youtube"}]`, `autoPublish: true`, `draft: false`.
   - `youtubeData`: `type "short"`, `privacy "public"`, `madeForKids false`, `isAiGeneratedContent false`, `category "EDUCATION"`, plus 5–8 tags.
   - Title: punchy, ≤60 characters, ending in ` #shorts`.
   - Text (the description): 1–2 sentence summary, then "Not medical advice." when a health claim is involved, then a `Sources:` line naming the studies or outlets, then 5 hashtags including `#shorts`.
   - Confirm the response's `media` was rewritten to `static.metricool.com` (that means Metricool fetched the video).
10. **Log in Clip Desk** with ArtifactData `batch` (op `set`, collection `clips`, doc_id `orig-YYYYMMDD-slug`): `title`, `creator: "Original Short, made by Claude"`, `sourceUrl` (the raw GitHub URL), `timestamp` (duration), `permission: "granted"`, `topic`, `hook`, `addedValue: "Fully original explainer with a reality-check beat."`, `notes` (scheduled slot and Metricool planner URL), `status: "scheduled"`, `addedBy: "scout"`, `scoutDate`, `createdAt`.
11. **Scout clip ideas.** Also add 3–5 clip ideas from popular wellness creators as `status: "idea"` (see the existing `seed-*` and `scout-*` docs for the fields). Prioritize open paid clipping campaigns (Whop, Content Rewards and similar). Use `permission: "program"` only for a real open campaign or published clipping policy.
12. **Report.** Finish with a short summary: the 2 videos (title, scheduled time, Metricool planner link), the reasoning for each topic, and any open paid clipping campaigns found. Remind the owner they can delete a post in Metricool before it goes live.

## If something fails

- Push refused: report it, and tell the owner to check the Claude GitHub app is still installed on the repo. Don't schedule anything.
- Metricool error: report the exact error, and still log the video in Clip Desk as `status: "editing"` with the error in `notes`.
- Never post anything you couldn't verify, and never invent sources.
