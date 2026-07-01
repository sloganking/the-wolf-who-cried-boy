# Model Timeline — provenance of AI-written work

Purpose: let a future model figure out **which language model wrote a given passage**, without burning tokens stamping every edit. (Pattern adapted from the private RPM repo's `model-timeline.md`.) Two cheap mechanisms, used together:

1. **Git dates + the tables below** — every line already has a commit date for free via `git blame -w -C`. Map that date to whichever model was in use → you know the model. Retroactive across all existing history, zero ongoing cost.
2. **A change-only log** (below) — a new row **only when the model in use changes**, not per session, per edit, or per commit. `wiki/log.md` already records *what* was done; this file only records *which model* was doing it.

**Why this matters:** a smarter model can later reassess older passages knowing which model era wrote them — e.g., re-reviewing chapters drafted in the Opus 4.6 era with fresh eyes.

## The default rule

> **A line was written by whichever model the "Model in use" table says was active on its git commit date — unless the Exceptions section says otherwise.**

Before 2026-07-01, Logan's working default was "always the newest Claude Opus," so the release-date table alone reconstructs that whole era. From 2026-07-01, model choice varies — the model-in-use table is the source of truth, and it only needs a new row when the model changes.

## Caveats (so this is trusted the right amount)

- **Bulk commits**: commits sometimes batch several days/sessions, so the commit date can lag the real authoring date — occasionally off near a boundary. Log an exception if it matters.
- **Reformatting reattributes lines**: a reflow/rewrite re-blames lines to the latest commit, erasing the original model's date. (`git blame -w -C` helps but isn't perfect.)
- **git blame can't tell human from AI**: it only knows the commit date, not whether Logan or the model authored the words. The date gives you the *model era*, not human-vs-model.
- **Forgotten switches are the failure mode of change-only logging**: if a model switch didn't get a row, the inference is silently wrong for that stretch. When discovered, fix it with an Exceptions entry rather than rewriting the table.
- **Self-report is unreliable**: models don't always know their own exact version. Rows reflect **the model actually selected in Cursor**, not what the model claims to be.
- **This repo is public**: anything written here follows the same rules as everything else — patterns and roles only, never real names of private individuals or anyone's role in real incidents.

---

## Opus release-date table (for the pre-2026-07-01 era)

This repo's first commit is 2025-12-31. Under the "always newest Opus" default, a line committed on/after a release date (and before the next) was written by that version.

| Model | Released | Notes |
|-------|----------|-------|
| Claude Opus 4.5 | 2025-11-24 | Current at repo creation (2025-12-31) |
| Claude Opus 4.6 | 2026-02-05 | 1M context |
| Claude Opus 4.7 | 2026-04-16 | New tokenizer, adaptive thinking |
| Claude Opus 4.8 | 2026-05-28 | Last model of the "always newest Opus" era |

*Opus release dates carried over from the RPM repo's verified table (checked against Anthropic announcements 2026-06-19).*

---

## Model in use (append a row ONLY when the model changes)

A row means: from this date, sessions in this repo use this model, until the next row. Do not add rows for sessions that continue with the same model.

| From | Model as selected in Cursor |
|------|------------------------------|
| 2025-12-31 | Newest Claude Opus available (see release-date table above) |
| 2026-07-01 | Claude Fable 5 (thinking, high) |

---

## Exceptions

Log here any time the tables above are wrong for a specific stretch — a one-off session with a different model, work committed long after it was written, a forgotten switch discovered later. Format: date range or commit(s), actual model, one line of context.

*(none yet)*
