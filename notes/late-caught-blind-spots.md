# Late-Caught Blind Spots

A log of things the book (and the collaboration around it) went a long time without checking — not ordinary edits, but whole categories of question that nobody thought to ask. Each entry records what was missed, how long it sat, how it finally got caught, and what *category* of blind spot it represents.

**The purpose of this file:** before publication, hand this list to fresh reviewers — human and AI — and ask: **"Here's the shit we missed for months. Is there anything else like any of these?"** The categories matter more than the specific catches: each one names a *direction nobody was looking*, and directions tend to hide more than one thing.

**Privacy rule (same as everywhere in this repo):** patterns and roles only. No real names of private individuals, no connecting any named person to any real incident.

---

## The catches

### 1. The legal system didn't exist in the book for most of its development

**What was missed:** The book built a complete apparatus for handling threats of violence — order of operations, removal, re-entry policy, refunds, telling the crowd — and for most of its development, none of it mentioned that a death threat is a *crime*. Not as a recommendation to call the police, not even as a fact the facilitator or target should know. The entire threat-handling system was container-native, as if the room were the only jurisdiction.

**How it got caught:** Late (mid-2026), through the author's own work on the false-accusation aftermath — researching where the law actually stands and discovering the inversion: the accidental touch the room treated as a crime wasn't one (criminal law requires intent), while the death threats the room tolerated were felony-eligible. That produced "Know Where the Law Actually Stands" (`when-youve-been-wronged.md`) and the severity-ranking paragraph in `handling-threats-of-violence.md`.

**Why it was missed:** The author's fear had inverted the legal map (the book now documents this honestly — he spent the incident terrified of a legal system that would have been his protection). And the industry's culture treats incidents as community matters by default; "call the cops" is close to unthinkable in spaces that distrust institutions. A blind spot shared by the author AND the culture AND every AI collaborator reading in the book's own frame.

**Category: interfaces with mainstream institutions.** The book is thorough *inside* the container. Where the container touches the outside world — law, medicine, insurance, mandated systems — coverage only exists where someone happened to look.

### 2. The Gun Test's name, spoken aloud in a live room

**What was missed:** The Gun Test is one of the book's named tools, published and shipped — and until 2026-07-05, nobody asked what happens when staff *say it out loud* at an event. "Gun check" spoken across a play party installs the word "gun" into participants who don't share the tool's context, in a room where some people are already scanning for danger. The book's own language teaching (what enters the mind shapes what the mind sees; don't repeat fiction) predicts the problem — and was never run against the book's own tool names.

**How it got caught:** The author imagined the deployment scene — walking up and saying "gun check" in front of participants — and felt the flinch.

**Fix (implemented 2026-07-05, `tools/gun-test.md`):** the Gun Test keeps its name (the gun is the teaching, and the question is never spoken as a call), but the interpersonal check was renamed **"The State Check"** — the section title is the spoken form, so reading rehearses the right words ("Gun Check" as a name is retired). No context-switching alias, because autopilot says the words you practice regardless of which room it's in (Target Focus Training's weapon-drop rule). Memory bridge: the question asks about your *state* and a *gun* → "gun state check" → speak the last half. All spoken scripts on the page are participant-safe. This matches how other fields solve it: surgery's "time out," diving's "buddy check," kink's "red" — the deployed token is neutral and identical to the tool's name; the vivid teaching lives in training material.

**Category: page language vs. room language.** Words designed for a reader can misfire when spoken in a live container. No one had swept the book's tool names and scripts for how they *sound in the room*.

### 3. Self-hosted clips of copyrighted footage, linked from the published book

**What was missed:** Google Photos links to the author's own uploads of TV scenes sat in the published web book as quote attributions ("[clip](...)"). Two exposures: linking to self-hosted copyrighted footage (unlike linking a YouTube video someone else posted), and the naked-pointer link format itself, which the writing guide bans because it renders as dangling "(clip)" text in print.

**How it got caught:** 2026-07-04, when the author was about to add another one and questioned the legality mid-request.

**Status:** resolved 2026-07-05 — the new instance was never published with the link, and the older instance (the First Officer quote in `walking-your-talk.md`) had its clip link removed the same morning. Clip URLs live in chat transcripts if ever needed internally. The *category* stays open for the pre-publish sweep: anything else embedded or linked that the author doesn't hold rights to.

**Category: rights and permissions.** Also connects to the standing pre-print item: quote-permission check for longer book excerpts (see `notes/fable-review-plan.md`, item H).

### 4. Transcript-derived quotes entering the book unverified

**What was missed:** The book has a verify-before-quoting practice (the Heinlein and *Greatest Showman* quotes were checked word-for-word against their sources before insertion) — but it wasn't applied automatically when the source was a *video transcript*. The SNW "acting captain" quote in `walking-your-talk.md` entered from an auto-generated transcript with garbles corrected by judgment, not by rewatching.

**How it got caught:** 2026-07-04, flagged during the same session that added it; logged as verify-before-print.

**Status:** open — the quote needs checking against the episode before the section counts as final.

**Category: sourcing discipline has format-shaped holes.** The practice existed; it just didn't fire for a source type nobody had named.

### 5. The author's own pattern wrote some of the prescriptions (the canonical specimen)

**What was missed:** The original advice in When You've Been Wronged said, in effect, "just inform the facilitator" — advice written *by the author's fawning pattern*, prescribing under-advocacy to readers in the exact situation where he had under-advocated. It sat in the book until the author caught it, corrected it, and published the catch itself as a teaching (the advocacy-gap passage).

**Why it's in this file:** it's the cleanest proof of the category, and the book itself treats it that way.

**Category: the writer's pattern authoring the advice.** Any prescription in the book could, in principle, be a pattern talking. The advocacy-gap catch shows what finding one looks like from the inside — worth asking reviewers: *where else might the author's documented patterns (fawning, fear of institutions, over-carefulness with accusers) have written the advice?*

---

## The pre-publish exercise

Hand reviewers the five categories, not just the five catches:

1. **Institutional interfaces** — What else lives where the container touches the outside world, unwritten? Candidate checks (unverified, listed as questions): When does a facilitator call emergency medical services — and does the book say so anywhere? Mandatory-reporting obligations for licensed professionals attending or staffing events? Intoxication where it intersects consent *law*, not just consent practice? Venue liability and insurance after an incident? Whether "document what happened" anywhere notes that documentation can become legal evidence — for either side?
2. **Page language vs. room language** — Sweep every named tool and script for how it sounds spoken aloud to people who haven't read the book. (The Gun Test is caught — its spoken form is now the state check; what does "influence firewall" sound like mid-event?)
3. **Rights and permissions** — The remaining clip link; the item-H quote-permissions sweep; anything else embedded that the author doesn't hold rights to.
4. **Sourcing discipline** — Any other quote that entered through a transcript, memory, or secondhand citation without a verification pass.
5. **The writer's pattern in the prescriptions** — Where might fawning, institutional distrust, or the author's specific history have shaped advice in ways a reader with different patterns would catch instantly?

And the standing meta-question for reviewers: **"What question has nobody in this project asked yet?"**

---

## Adding entries

When something surfaces that fits — a whole direction nobody was looking, not a routine fix — add it here with: what was missed, how long it sat, how it got caught, the fix/status, and above all the **category**. Log the addition in `wiki/log.md`.
