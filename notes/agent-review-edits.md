# Agent Review Edits — June 2026 Full-Book Read

Findings from a complete read of all 41 source files plus link audit, site check, and repo review.
Separate from `production-checklist.md` (overlaps noted where they exist).
Run `python scripts/check_links.py` to re-verify link fixes — run it before every push.

---

## Done

- [x] **Intro banner removed from top** — the book now opens with its actual opening lines. A small neutral "A Note on This Edition" sits at the end of the intro (web edition / continuously updated / print + ebook + audiobook coming). No "living book" branding. (`src/introduction.md`)

---

## Urgent — reader-facing bugs (do before wider sales / Laurie)

- [x] **Fix the one real 404:** `when-youve-been-wronged.md` → `../tools/rbdsmt.md` retargeted to `./before-play.md#rbdsmt-the-safer-sex-conversation`. Verified with link checker — zero missing files remain.
- [x] **Compress `src/images/logan.jpg`** — 12.4 MB → 179 KB (3648×5472 → 750×1125, JPEG q85). Original retrievable from git history if needed for print.
- [x] **Fix 26 broken anchors** — DONE in one pass. 21 retargeted to the renamed/relocated headings below; 5 fixed by inserting invisible `<a id="...">` anchors at the exact spot (no visible content changed): `i-would-never-do-that` (body-stories), `find-your-compass` (i-made-a-mistake), `your-voice-matters` (responsibility), `belief-shattering` (healing-fawning), `serving-not-pleasing` (walking-your-talk). `scripts/check_links.py` (now HTML-anchor-aware) reports **zero broken internal links across all 41 files**. Original mapping table kept below for reference:

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

- [x] **Delete `src/concepts/making-it-right.md`** — orphaned 10-byte stub, deleted.
- [x] **`src/examples.md`** — moved to `notes/examples.md` with a status/plan note at the top: vestigial as a chapter, kept as seed material for the future field manual (its end-to-end worked-scenario format is the field manual's spine).
- [x] **`back-cover-blurb.md`** — moved `src/` → `notes/` (git mv), no longer in the published site output.
- [ ] **`before-you-facilitate.md` has no "Related" section** — only chapter that ends without one (just `---`). Content itself is complete (verified, not truncated — also closes the open question in `production-checklist.md` → Structural).
- [x] **Link check in CI** — `scripts/check_links.py` now exits 1 on failure, and `deploy.yml` runs it before the build. A push with broken links fails the workflow (GitHub emails the failure), and the live site stays on the last good version.

---

## Content additions (optional, post-release ordering)

- [ ] **"When the Accuser Is Right" — short section, not a chapter.** Author's read: the industry's biggest problem is righteous predators harming the undeserving, and the book already teaches "act — just verify first." Agreed on both. The section's job isn't to rebalance the book — it's rhetorical armor: it closes the exit a hostile reader uses to dismiss the whole thing ("this book only protects the accused"). ~800–1,500 words walking the path where verification *confirms* the harm: pattern severity, proportional removal, supporting the harmed person without becoming a mob. Candidate home: end of `before-you-judge.md` (after "When You Can't Verify") or inside `appropriate-response.md`. Worth doing before retreat-table sales, where survivor-advocacy-minded readers will be in the audience.
- [ ] **"Identity Precedes Action" (from TODO.md)** — already ~80% present across `i-made-a-mistake.md` (Protect Your Identity, What Gets Born). Remaining 20% fits as a short section in `when-youve-been-wronged.md`, not a new page.
- [ ] **Power Debt personal paragraph clarity** (`all-power-is-mutual.md`) — author flagged: "You're holding the power debt right now" is imprecise. The fix is conceptual, ~3 sentences, not a flesh-out: distinguish *accrual* (happens silently, needs no witnesses — the debt existed the night of the retreat even though nobody believed him) from *collection* (needs an audience — the book is the collection vehicle, each reader is the debt paying out). Also make explicit: the debt is being spent on the *pattern*, not the *person* — collecting wisely vs. destructively, per the section's own taxonomy. Author voice required; draft offered in chat as starting material.
- [ ] **Companion field manual** — 15–20k words, pure protocol: flowcharts, checklists, three-sentence scripts, the 2 AM document. Write AFTER the main book ships and link targets stabilize. Distill from Quick Reference + response flowchart + the Promise + threats-of-violence walkthrough. Same repo to start; decide packaging later.

---

## Launch Sequence (decided June 2026)

The path from "9 manual sales" to "scalable product." Vision: ebook + paperback + audiobook on Amazon/Google Play/Audible. The web edition is interim product now, free sample later.

1. - [ ] **Write the buyer list (today, 10 min).** One spreadsheet/file: name + email of all 9 buyers. Every future buyer gets appended. This is the artifact that lets you give early buyers the first-edition ebook free later — no remembering required.
2. - [ ] **Interim scalable sales (tonight, ~30–60 min): Gumroad.** Product = "The Wolf Who Cried Boy (Web Edition)" at chosen price; deliverable = a 1-page welcome PDF containing the site link (+ note that buyers get the first-edition ebook free when it ships). Buyers pay → instant automatic delivery → Gumroad keeps the buyer list. Replaces PayPal-then-manually-verify-then-manually-send. Doesn't solve link-sharing security — accepted; this is a bridge, retired at Amazon launch. Fallback if Gumroad's content review balks: Payhip.
3. - [ ] **Polish pass** — `production-checklist.md` "Three Things" (advocacy-gap remainder, tightening pass, quick fixes) + final sweeps. Content freeze at the end. Amazon reviews are permanent; launch the version a stranger can review.
4. - [ ] **CANNOT-SKIP items before Amazon:** quote-permission screenshots (Laurie + Enki), legal review of the private-message quotes in `drama-triangle.md` (matters MORE for Amazon than for the website).
5. - [ ] **EPUB conversion** — pandoc pipeline from existing markdown (agent task, free). Internal links survive in EPUB.
6. - [ ] **KDP ebook launch at \$9.99** (70% royalty band ends at \$9.99 — \$9.99 earns ~\$7/sale, \$14.99 earns ~\$5.25). Email the EPUB free to everyone on the buyer list.
7. - [ ] **Paperback (after ebook):** KDP print-on-demand — no inventory. Needs a separate fixed-layout interior + wraparound cover. OUTSOURCE the formatting (see below). Paperback carries the \$15–25 price positioning.
8. - [ ] **Retire the free full site:** repo → private; public site becomes a free-sample edition (intro + 1–2 chapters + "buy on Amazon"); coaching site points at the sample. Leak window closes permanently here.
9. - [ ] **Post-launch ideas (parked):** linked web edition as premium tier / buyer bonus ("professional tool" — the cross-link web is the feature print can't replicate); companion field manual (seed: `notes/examples.md`); audiobook (ACX/Findaway).

**Outsourcing (high leverage, low burn):** paperback interior formatting ≈ \$200–800 freelance (Reedsy/Upwork), or DIY-ish with Atticus (~\$150 one-time). Cover design ≈ \$100–500 (see `notes/cover-design.md`). Total launch outsourcing budget ≈ \$500–1,500. Rule: don't hire formatting until content freeze (step 3) — formatting before freeze = paying twice. Ask the aunt who publishes what she uses first.

- [ ] **Laurie / retreat sales readiness** — the bar before the book is sold at ISTA-adjacent retreats: steps 3–4 above + "When the Accuser Is Right" section.
