# Model Timeline — provenance of AI-written work

Purpose: let a future model figure out **which language model wrote a given passage**, without burning tokens stamping every edit. (Pattern borrowed from the private RPM repo's `model-timeline.md`.) Two cheap mechanisms, used together:

1. **Git dates + a release-date table** (below) — every line already has a commit date for free via `git blame`. Map that date to whichever model was current under the default rule → you know the model. Retroactive across all existing history, zero ongoing cost.
2. **A session log** (below) — appended when a chat does substantive work in this repo. This is the ground-truth backstop for when the git-date inference is wrong or ambiguous (bulk commits, version-boundary dates, or when a non-default model was used).

**Why this matters here specifically:** a smarter model can later reassess older passages knowing which model era wrote them — e.g., re-reviewing chapters drafted in the Opus 4.6 era with fresh eyes. `git blame -w -C <file>` gives the per-line dates.

## The default rule

> **Before 2026-07-01: assume a line was written by the latest Claude Opus model available as of its git commit date — unless the session log or exceptions say otherwise.**
>
> **From 2026-07-01 onward: the "always newest Opus" default no longer holds — model choice varies by session. Check the session log; if a date has no entry, treat the model as unknown rather than assumed.**

## Caveats (so this is trusted the right amount)

- **Bulk commits**: commits sometimes batch several days/sessions, so the commit date can lag the real authoring date — occasionally off near a version boundary. The session log resolves these.
- **Reformatting reattributes lines**: a reflow/rewrite re-blames lines to the latest commit, erasing the original model's date. (`git blame -w -C` helps but isn't perfect.)
- **git blame can't tell human from AI**: it only knows the commit date, not whether Logan or the model authored the words. The date gives you the *model era*, not human-vs-model.
- **Self-report is unreliable**: models don't always know their own exact version. Session-log entries reflect **the model actually selected in Cursor**, not what the model claims to be.
- **This repo is public**: session-log descriptions follow the same rules as everything else here — patterns and roles only, never real names of private individuals or anyone's role in real incidents.

---

## Release-date table (date → model)

This repo's first commit is 2025-12-31. A line committed on/after a release date (and before the next) was written by that version, under the default rule.

| Model | Released | Notes |
|-------|----------|-------|
| Claude Opus 4.5 | 2025-11-24 | Current at repo creation (2025-12-31) |
| Claude Opus 4.6 | 2026-02-05 | 1M context |
| Claude Opus 4.7 | 2026-04-16 | New tokenizer, adaptive thinking |
| Claude Opus 4.8 | 2026-05-28 | Last model under the "always newest Opus" default |
| Claude Fable 5 | — | First used in this repo 2026-07-01; from here on, rely on the session log |

*Opus release dates carried over from the RPM repo's verified table (checked against Anthropic announcements 2026-06-19). When a new model enters use here, add a row and a session-log entry.*

---

## Session log

Append one line per chat that does substantive work. Format:

`YYYY-MM-DD HH:MM (TZ) — <model as selected in Cursor> — <one-line what the session did>`

- 2026-07-01 14:02 (UTC-7) — Fable 5 (thinking, high) — first Fable 5 session in this repo: read the entire book in one context window; produced the full-book review (ratings, industry prediction, to-do list) → captured in `notes/fable-review-plan.md`; expanded `wiki/.private-context.md`; created this file; cleaned a stale `.gitignore` entry

---

## Exceptions

Log here any time the default rule is wrong for a stretch of history — e.g., an older model, a non-Claude model, or work committed long after it was written.

*(none yet)*
