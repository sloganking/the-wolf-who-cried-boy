# Agent Review Edits — June 2026 Full-Book Read

Findings from a complete read of all 41 source files plus link audit, site check, and repo review.
Separate from `production-checklist.md` (overlaps noted where they exist).
Run `python scripts/check_links.py` to re-verify link fixes — run it before every push.

---

## Done

- [x] **Intro banner removed from top** — the book now opens with its actual opening lines. A small neutral "A Note on This Edition" sits at the end of the intro (web edition / continuously updated / print + ebook + audiobook coming). No "living book" branding. (`src/introduction.md`)

---

## Urgent — reader-facing bugs (do before wider sales / Laurie)

- [ ] **Fix the one real 404:** `when-youve-been-wronged.md` links to `../tools/rbdsmt.md`, which doesn't exist. Retarget to `./before-play.md#rbdsmt-the-safer-sex-conversation`.
- [x] **Compress `src/images/logan.jpg`** — 12.4 MB → 179 KB (3648×5472 → 750×1125, JPEG q85). Original retrievable from git history if needed for print.
- [ ] **Fix 26 broken anchors** (silent fails — reader lands at top of page instead of the section). Suggested retargets:

| File | Broken link | Suggested fix |
|---|---|---|
| `all-power-is-mutual.md` | `./drama-triangle.md#victim` | `#the-three-roles` |
| `before-play.md` | `./trauma-and-filters.md#the-brownred-exercise` | `#try-this-right-now` |
| `before-you-facilitate.md` | `./before-play.md#the-friction-check` | `#the-friction-check-interpretive-compatibility` |
| `before-you-facilitate.md` | `./walking-your-talk.md#serving-not-pleasing` | `#the-gap-between-knowing-and-being` (or add a "Serving, Not Pleasing" heading there) |
| `before-you-facilitate.md` | `#threats-of-violence-must-be-stopped-immediately` (in-page) | `./when-things-go-wrong.md#threats-of-violence-must-be-stopped-immediately` |
| `from-threat-to-ally.md` | `./trauma-and-filters.md#when-the-feeling-comes-first` | `./body-stories.md#when-the-feeling-comes-first` |
| `guiding-public-repair.md` | `#three-sentences-then-you-leave` | `#speaking-truth-instead-of-fawning` |
| `handling-threats-of-violence.md` | `#to-the-crowd` | `#what-to-say-to-the-crowd` |
| `healing-fawning.md` | `./i-made-a-mistake.md#find-your-compass` | promote bold "**Find your compass.**" to a real heading, or retarget `#when-you-were-the-righteous-predator` |
| `healing-fawning.md` | `#how-the-pattern-breaks` | `#the-pattern-that-heals` |
| `healing-fawning.md` | `#the-two-victims-problem` | `./fawning.md#the-two-victims-problem` |
| `healing-fawning.md` | `#the-empowered-fawners-practice` | `./fawning.md#the-empowered-fawners-practice` |
| `healing-fawning.md` | `./invisible-patterns.md#the-question-underneath-the-sentence` | `#your-primary-question` |
| `healing-fawning.md` | `#belief-shattering` | `#practice-saying-yes-to-your-own-desire` |
| `i-made-a-mistake.md` | `./body-stories.md#i-would-never-do-that` | promote `**Example: "I Would Never Do That"**` to a heading, or retarget `#stories-and-the-problems-they-create` |
| `invisible-patterns.md` | `./body-stories.md#i-would-never-do-that` | same as above |
| `i-made-a-mistake.md` | `./responsibility.md#responsibility--repair` | `#responsibility-is-not-repair` |
| `repair.md` | `./responsibility.md#responsibility--repair` | `#responsibility-is-not-repair` |
| `repair.md` | `./types-of-mistakes.md#unconscious-mistakes` | `#why-unconscious-mistakes-happen` |
| `power-dynamics.md` | `./invisible-patterns.md#complementary-filters` | `#when-filters-find-each-other` |
| `trauma-and-filters.md` | `#the-brownred-exercise` (in-page) | `#try-this-right-now` |
| `when-things-go-wrong.md` | `#the-promise` (in-page, 2 spots in Emergency Exception) | `./before-you-facilitate.md#the-promise` |
| `when-youve-been-wronged.md` | `./drama-triangle.md#victim` | `#the-three-roles` |
| `when-youve-been-wronged.md` | `./drama-triangle.md#creator` | `#the-empowerment-shifts` |
| `when-youve-been-wronged.md` | `./responsibility.md#your-voice-matters` | promote the Asch-experiment paragraph to a "Your Voice Matters" heading, or retarget `#examples-of-taking-responsibility-for-others-mistakes` |
| `why-helping-is-hard.md` | `./when-youve-been-wronged.md#set-boundaries-about-how-youre-spoken-to` | `#dont-fawn` |

---

## Housekeeping

- [ ] **Delete `src/concepts/making-it-right.md`** — 10-byte stub ("# Repair"), orphaned, nothing links to it.
- [ ] **Decide `src/examples.md`** — three good worked scenarios, currently invisible (not in SUMMARY, not linked). Recommendation: add to the Reference section of SUMMARY after Quick Reference. Alternative: cut it.
- [ ] **`back-cover-blurb.md`** — working file living in `src/`; mdBook copies src files to the published output, so it's fetchable by URL. Move to `notes/` if you don't want it publicly reachable.
- [ ] **`before-you-facilitate.md` has no "Related" section** — only chapter that ends without one (just `---`). Content itself is complete (verified, not truncated — also closes the open question in `production-checklist.md` → Structural).
- [ ] **Optional: add link check to CI** — one extra step in `.github/workflows/deploy.yml` running `scripts/check_links.py` so broken links can never ship again.

---

## Content additions (optional, post-release ordering)

- [ ] **"When the Accuser Is Right" — short section, not a chapter.** Author's read: the industry's biggest problem is righteous predators harming the undeserving, and the book already teaches "act — just verify first." Agreed on both. The section's job isn't to rebalance the book — it's rhetorical armor: it closes the exit a hostile reader uses to dismiss the whole thing ("this book only protects the accused"). ~800–1,500 words walking the path where verification *confirms* the harm: pattern severity, proportional removal, supporting the harmed person without becoming a mob. Candidate home: end of `before-you-judge.md` (after "When You Can't Verify") or inside `appropriate-response.md`. Worth doing before retreat-table sales, where survivor-advocacy-minded readers will be in the audience.
- [ ] **"Identity Precedes Action" (from TODO.md)** — already ~80% present across `i-made-a-mistake.md` (Protect Your Identity, What Gets Born). Remaining 20% fits as a short section in `when-youve-been-wronged.md`, not a new page.
- [ ] **Companion field manual** — 15–20k words, pure protocol: flowcharts, checklists, three-sentence scripts, the 2 AM document. Write AFTER the main book ships and link targets stabilize. Distill from Quick Reference + response flowchart + the Promise + threats-of-violence walkthrough. Same repo to start; decide packaging later.

---

## Product / distribution

- [ ] **Access model** — currently honor-system (public repo, free link on coaching site, paid link sent to buyers). Fine for 9 sales; move to a real delivery method before scaling, and update existing buyers when it changes. (Author's own note.)
- [ ] **Laurie / retreat sales readiness** — the bar before the book is sold at ISTA-adjacent retreats: all items in "Urgent" above, plus the quote-permission screenshots and legal review already tracked in `production-checklist.md` (Quote Permissions, Legal Review — both marked CANNOT SKIP there).
