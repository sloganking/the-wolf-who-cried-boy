---
title: Wiki Log
tags: [meta]
updated: 2026-07-01
---

# Wiki Log

Append-only record of wiki changes. Each entry starts with a consistent prefix for parseability.

---

## [2026-07-01] add | Full-book review captured → `notes/fable-review-plan.md`; `.private-context.md` expanded

**What happened:** A Fable 5 model read the entire book (all 162k words) in one context window and produced a full analysis — overall/chapter ratings, industry-impact prediction, ship-readiness, celebrations, coaching prediction, and a to-do list. The author reviewed it and made decisions. Everything is captured in `notes/fable-review-plan.md` (the handoff doc for future sessions — **start there before doing any of the review work**).

**Headline decisions:** (A) write a new "When It's Actually a Wolf" chapter — protocol for verified malice, no deep predator psychology needed; (B) split the intro's Perception & Prescription note — compressed perception paragraph stays in intro, prescription/vantage statement moves to top of `before-you-facilitate.md`; (C) cool + tighten the apology dissection in `repair.md`; (D) retier hard facilitator prescriptions as principle/full/minimum (Gun Check is the model) — keep authoritative voice, add gradations; (E) make the "hungry ghost" staff check procedural/behavioral; (F) build a Facilitator Field Review Packet instead of asking facilitators to read the whole book; (G) two-edition strategy — hyperbook stays maximal, condensed print edition later.

**Privacy:** `wiki/.private-context.md` (gitignored) expanded with the full no-names rules for private individuals connected to real incidents — read it before writing anything in this public repo. Verified all private notes files are untracked and tracked history is clean.

**Also this session:** created `model-timeline.md` at the repo root (model provenance via `git blame` + a change-only "model in use" table — add a row ONLY when the model changes, never per session/edit/commit) and wired the session-start check into `wiki/index.md`'s "For AI assistants" block so every future session sees it. Wrote `notes/real-wolf-chapter-brief.md` (full brief for the "When It's Actually a Wolf" chapter) while the whole book was in context.

**Files updated:** `notes/fable-review-plan.md` (new), `notes/real-wolf-chapter-brief.md` (new), `model-timeline.md` (new), `wiki/index.md` (model-provenance check added), `wiki/.private-context.md` (expanded, gitignored), `wiki/log.md` (this entry).

---

## [2026-06-29] edit | `invisible-patterns.md` — Narrative Lock signal #3 expanded to "No Real Repair Path" (+ painted-on door / domestication-through-shame)

**Book change:** Renamed Narrative Lock's third signal from **No Repair Path** to **No Real Repair Path** and split it into two failure modes: the **closed door** (the original — "I'm done," no future repair) and the **painted-on door** (new — a path *appears* to exist, but the only way through is to agree with the story: accept the assigned motive, confirm the category, take on the label). Distinction drawn: real repair asks you to own *what you did* (a behavior/impact); a painted-on door asks you to ratify *who they've decided you are* — a confession demanded as its price, i.e. the [[fawning]] the book already warns about, charged as a toll for reentry. Added the cost mechanism: taking on a degrading label to make an angry person stop is **domestication through shame** (label = leash, compliance = rewarded behavior, each success lowers the bar for the next demand), and the exact route by which a story about *what you did* hardens into [[sinsickness]] about *who you are* — a verdict installed by someone else and carried by you. Also added a symmetric self-check question (#4: is the "way back" I'm offering real, or a painted-on door?) so the lens turns back on the reader, per the chapter's existing turn-it-around move.

**Writing-guide check:** framed from the target's side (what accepting the label does to *you*) to stay inarguable and non-moralizing; "domesticate" used once as a plain descriptive verb, not coined/bolded as a Defended Term; used a bracketed placeholder ("[what they called you]") instead of parading a specific label, per "Don't Repeat Fiction." Origin: a real coaching incident (worked through in the author's private notes) — a narrative-locked "repair path" whose only way back required accepting a "you're not a man, you're a boy" label.

**Files updated:** `src/concepts/invisible-patterns.md` (signal #3 + self-check), `wiki/narrative-lock.md` (signal #3 + self-check), `wiki/glossary.md` (Narrative Lock entry + new **Painted-On Door** entry), `wiki/log.md` (this entry).

---

## [2026-06-25] add | `trauma-and-filters.md` — new "Everything Has Everything In It" subsection + two coined terms

**Book change:** Added a `### Everything Has Everything In It` subsection to `src/concepts/trauma-and-filters.md` (under "Stories Control Attention," after the brown-red/RAS exercise, before "The Horror Movie Effect"). Coins **everything has everything in it** (every person/situation holds all qualities at once — beauty and ugliness, hope and despair — and your attention selects which side, which becomes belief → feeling → action) and **factually selective** (accurate about the side you're focused on, blind to the side you're not). Extends the chapter's existing attention→story→feeling chain with the everything-contains-everything premise and the →action tail. Kept tight (3 paragraphs) to extend rather than restate the RAS/elephant material. No external attribution (Tony Robbins already quoted in-section for the same root idea; the lead distinction is the author's). Glossary updated under E and F.

---

## [2026-06-25] add | `all-power-is-mutual.md` — new "Selfless Defense" section + coined term

**Book change:** Added a `### Selfless Defense` subsection to `src/concepts/all-power-is-mutual.md` (after `### Power Debt`, before `## The Practical Takeaway`). Coins **selfless defense** (a play on self-defense): the same action — standing your ground — but sourced from protecting everyone the precedent would reach, not only yourself. Built on the author's retreat story already in Power Debt; names the selfish desire honestly (links [[why-helping-is-hard|Humans Are Suspicious of Selflessness]] — hiding self-interest erodes trust), admits self-interest alone might not have been enough to stay, then reveals the selfless motive ("the largest reason I did it was for them — and everyone who would come after"). Notes the better in-the-moment move (links `when-youve-been-wronged#show-your-humanity`) and the precedent cost (links `punishment-culture.md`). Deliberately avoids labeling all attackers "narrative-locked" ("even the ones attacking me ... even though they couldn't see it") to stay inarguable. Glossary updated under S.

---

## [2026-06-23] edit | `100-percent-control.md` — merged "This Works Both Ways" into "The Two-Sided No"

**Book change:** Merged the `This Works Both Ways` and `The Two-Sided No` subsections into a single `The Two-Sided No` section in `src/tools/100-percent-control.md`. The two sections each walked the prevent/create split separately (redundant restatement); now the split is established once and framed through the two-sided-no lens. All distinct content preserved (the "anything you want — just not with whoever you want" line, the `responsibility#the-dice-principle` link, "shape the odds / inevitable"). Wiki `hundred-percent-control.md` substance unchanged and still accurate.

---

## [2026-06-23] sync | `100-percent-control.md` — "The Two-Sided No" section added

**Book change:** Added a "The Two-Sided No" subsection to `src/tools/100-percent-control.md` (after "This Works Both Ways"). Names both halves of 100% control as forms of *no*: the **no to presence** (refuse what you don't want — spoken, then action/leaving if not respected) and the **no to absence** (refuse the *lack* of what you want — said by acting until the absence ends; the dance: keep asking until a yes). The reframe: the creation/persistence half *is* a no, and naming it turns a passive wait into an owned action. Wiki `hundred-percent-control.md` updated to match; relates to [[gift-of-no]].

---

## [2026-05-01] sync | `types-of-mistakes.md` harmful-belief section

**Book change:** Personal hickey / harmful-belief example expanded; added explicit link to [[filters-and-ras|Trauma & Filters]] (meaning vs. event) and parallel to Christopher Ryan concubine example; cultural framing (men and women; some women romanticizing *couldn't help himself*) without moralizing eras.

---

## [2026-04-14] create | Initial wiki build

**Scope:** Complete wiki created from a full read of the entire book.

**Pages created (39):**
- Meta (4): `index.md`, `glossary.md`, `book-overview.md`, `log.md`
- Concepts (25): `righteous-predator`, `narrative-lock`, `sinsickness`, `belief-blindness`, `fawning`, `reverse-fawning`, `body-stories`, `filters-and-ras`, `complementary-filters`, `drama-triangle`, `vulnerability-flip`, `top-and-bottom-vulnerability`, `conservation-of-power`, `two-victims-problem`, `gift-of-no`, `severity-model`, `mistake-matrix`, `responsibility-triad`, `over-and-under-response`, `replacing-the-sentence`, `witch-hunt-dynamic`, `the-promise`, `harmless-is-not-peaceful`, `fear-creates-what-it-fears`, `hiding-the-wound`
- Tools (6): `notice-feel-story`, `gun-test`, `influence-firewall`, `hundred-percent-control`, `rbdsmt`, `friction-check`
- Themes (3): `sight-vs-punishment`, `power-flows-both-ways`, `the-medium-is-the-message`
- Author: `author-logan-king`

**Source material read:** Every chapter of the book in full — introduction, rescue-that-made-me-see, all 28 concept files, all 4 tool files, conclusion, examples, quick-reference. Plus notes/book-terminology.md, notes/book-intent.md, notes/writing-guide.md, notes/book-notes.md, backstory.md.

**Decisions made:**
- Flat wiki structure (all pages in `wiki/`) for clean Obsidian graph
- `[[wikilinks]]` for Obsidian compatibility
- YAML frontmatter with tags for filtering
- Glossary as single alphabetical file (not split by category)
- One page per coined term / framework / tool
- Cross-references at bottom of every page
