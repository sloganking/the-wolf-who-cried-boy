# Writing Guide Catches

Append-only ledger of real sentences that failed a writing-guide rule and what they became. The guide states the rules; this file is the case law. Read it to calibrate what passes and what doesn't — the rules are abstract, these are the actual misses.

**Maintenance:** every time a catch is made (by the author or an AI co-author), append an entry here. Newest first. Keep entries short: what was written, which rule it broke and why, what it became. A few entries also live inline in the guide where they teach a specific rule — that's fine; this file is the aggregate.

---

## [2026-07-08] Legal jargon invisible to a fluent cold reader | `handling-threats-of-violence.md`

- **Written:** "a guard is the property owner's agent, with the same legal powers as any other private person" (and in the checklist: "a guard is the property's agent, not an officer").
- **Rule broken:** the plain-English standard the fresh-reader test exists to enforce — "agent" is a law word wearing an everyday word's clothes. The writer imported it straight from the legal sources. The author caught it; the cold reader that session did NOT — because that run used a mid-size fluent model, which understands legal register too well to stall on it. This is the protocol's own warning proven in the field: **being small is the feature.** A capable model is a bad proxy for the target reader.
- **Became:** "a guard has exactly the powers everyone else has — the uniform adds nothing" / "a guard has exactly the powers you have." A re-run with the smallest available model then caught what the fluent one also missed: a double negative ("no power it doesn't give everyone else"), a sequence referenced but never named ("minus the middle step" — now "words, then hands, then police"), and a conclusion that jumped ("so agree beforehand" — now carries its reason: the line is a judgment call and mid-crisis is a bad time to draw it).

## [2026-07-08] Unverified legal claim echoed as fact | `handling-threats-of-violence.md`

- **Written:** "reporting a crime, or calling 911 about danger, needs no property rights at all. Anyone can make those calls." — written into the Local-Law Checklist because the author assumed it and the AI co-author echoed it, with no source checked by either.
- **Rule broken:** Stand on Ground You Actually Hold, applied to facts. An echoed assumption is borrowed authority even when the borrowing is from the author himself — the co-author's job was verification, and agreement isn't verification. Author's catch: "I assumed this was true, so I said it. You seem to be repeating my words."
- **Became:** the sentence survived — verification confirmed it (anyone can report: victims, witnesses, third parties). What changed is the process: legal claims now get researched before they ship, and every researched question + answer + sources goes in `notes/legal-references.md`, which also lists the book's pre-existing legal claims still awaiting a verification pass.

## [2026-07-08] Implicit universal about facilitators | `handling-threats-of-violence.md`

- **Written:** "A facilitator has no enforcement mechanism beyond the container's own agreements."
- **Rule broken:** Martian check — an implicit universal. True of a retreat with a facilitation team; false of an arena event with a security staff. The author's first instinct was to soften to "most/many facilitators" — but uncounted counts fail the same check. The guide's own fix applies: enumerate the cases.
- **Became:** "If your event has security, they can walk someone to the door; when someone won't be walked, even security hands it to the police. A facilitation team without security just reaches that handoff sooner." — both cases named, unified by the author's insight that every enforcement ladder tops out at the same place; security only changes how many rungs you own.

## [2026-07-08] Oblique closer the reader must decode | `handling-threats-of-violence.md`

- **Written:** "And a container everyone knows will never call, no matter what, has told its most dangerous member exactly how far things can go."
- **Rule broken:** not a named rule — a first-pass failure. The point (a container that never calls demonstrates that violence has no ceiling here) arrives only after the reader assembles an inference from "told... exactly how far things can go." The sentence performs the insight instead of delivering it. Author: "there's a way to 10x those words... the old one was ambiguous."
- **Became:** "And a container that will never call, no matter what happens, is showing the most dangerous person in the room something true: however far they push, words are the only thing that will ever push back." — "showing" (the book's own walking-your-talk mechanism), and the consequence stated instead of gestured at.

## [2026-07-08] Compressed abstraction out of voice | `handling-threats-of-violence.md`

- **Written:** "The stance this book has held all along doesn't change here — it completes: internal handling for mistakes, external backstop for crimes. That's proportionality, applied to institutions."
- **Rule broken:** voice. "It completes," the noun-pile parallel, and "institutions" are academic register — no human says this across a table, and the book's voice is a human talking (Author Voice & Personality). Author: "this doesn't sound like me... not clear what it's telling me."
- **Became:** "None of this contradicts the stance this book has held all along — it's the same stance, reaching a different severity. Mistakes get repair, not punishment. Crimes get a response that matches their severity — and that response doesn't live inside the container."
- **The test this adds:** would the author say the sentence out loud to a facilitator friend across a table? If it only works on paper, it's out of voice.

## [2026-07-08] Uncounted absolute in a heading | `handling-threats-of-violence.md`

- **Written:** "### Why Nobody Calls"
- **Rule broken:** Martian check — "nobody" is a frequency claim nobody counted, and in a heading it paints a narrative about these communities. Author: "'nobody calls' is painting another narrative."
- **Became:** "### Why People Don't Call" — describes the pattern without the count. Headings get the Martian check too.

## [2026-07-08] Metaphor word carried past its home sentence | `handling-threats-of-violence.md`

- **Written:** "Located, they work the way the promise works everywhere else... Unlocated, the question gets asked for the first time..." — reusing the fire-exit metaphor's verb as the grammatical spine of the following sentences.
- **Rule broken:** not a named rule yet — a clarity miss, sibling of the "charisma as a verb" catch. The metaphor earns its home sentence ("located before the event, hopefully never used, known cold"), but carrying its vocabulary forward makes the reader translate the metaphor instead of following the point — you don't "locate" a decision to call 911. Author: "locating the 911 doesn't really make sense completely in language."
- **Became:** "Decided in advance, they work..." / "Left undecided, the question gets asked for the first time mid-crisis..." — plain words carry the parallel; the metaphor stays where it was made.

## [2026-07-08] Verdict-flavored opposition | `handling-threats-of-violence.md`

- **Written:** "the exact conditions that produce fawning instead of facilitating."
- **Rule broken:** No Moralizing Language / Martian verdict language. "Fawning instead of facilitating" implies the fawning facilitator has stopped being a facilitator — a verdict about the person smuggled in as a contrast. (The existing heading "Warning Signs You're Fawning Instead of Facilitating" survives because it's the reader examining themselves in a diagnostic; pointed at a third-person facilitator mid-crisis, the same opposition reads as judgment.) Author: describe the pressure, not the failure — "conditions that make it easier for facilitators to fawn."
- **Became:** "under exactly the pressures that make fawning easiest" — pressure acting on a person in a state; no claim about what they are or stopped being.

## [2026-07-07] Verdict-first framing | book pitch language (caught during the RPM book-description session)

- **Written:** "human conflict dynamics and false accusations" as the standing answer to "what's the book about?" — and, earlier, an author outreach message that led with the same false-accusation framing (the distinction arrived after it was sent).
- **Rule broken:** Don't Lead With the Verdict (this catch created the rule; the author supplied the mechanism: "if you say 'someone gave me false accusations,' people will ask inside 'is it false though?' Same problem as 'I was called a predator'"). "False" is a contested verdict a first-contact listener can't verify, so their first inner move is adjudication, not curiosity.
- **Became:** verdict-free openers — "Most harm doesn't come from bad people; it comes from good people who can't see what they're doing," and the village-finds-a-wolf image. Events and mechanisms stated; the verdict left for the listener to reach.

## [2026-07-06] Arguable label on a person | `before-you-facilitate.md`

- **Written:** "If you're sexually starved, you're a liability." (bolded section opener)
- **Rule broken:** No Moralizing Language / Inarguable Writing. "You're a liability" is a verdict about what a person *is*, and it's arguable — a starved reader can reject the label and the mechanism with it. The companion phrase "makes them a liability in intimate spaces" did the same to staff.
- **Became:** "If you're sexually starved, you're working impaired." Impairment describes function in a state (same frame as drunk driving, sleep deprivation — and the paragraph already closes on the sleep-deprived comparison), not what the person is. The staff phrase became "that starving, seeking, desperate-for-connection state where the animal body is back in charge" — pointing at the state and echoing the buffet-dog mechanism instead of labeling the person.

## [2026-07-06] Ambiguous pointer | `before-you-facilitate.md`

- **Written:** "friction-check no one harder than this person" — immediately after sentences containing a flight surgeon and a commander, giving "this person" three candidate referents.
- **Rule broken:** Name the Referent (this catch created the rule). If a pointer word can bind to more than one antecedent, the reader guesses or stalls.
- **Became:** "friction-check no one harder than your specialist."

## [2026-07-06] Cute verbing reads as odd slang | `before-you-facilitate.md`

- **Written:** "the commander doesn't charisma them back into the cockpit" — using "charisma" as a verb.
- **Rule broken:** not a named rule yet, but a voice miss: reaching for a cute coinage instead of the plain word draws attention to the sentence's cleverness instead of its point, and reads as odd rather than sharp.
- **Became:** "the commander can't simply order them back into the cockpit" — plainer, and it names the actual mechanism (an order doesn't override the medical call) instead of performing a verb trick.

## [2026-07-06] Fiction cited where a real system exists | `before-you-facilitate.md`

- **Written:** "*Star Trek* builds this pattern into Starfleet regulation — the ship's doctor serves under the captain everywhere except medical matters..."
- **Rule broken:** Stand on Ground You Actually Hold, applied to sources. A real system that demonstrably works carries the credibility claim; fiction only gestures at it. Also a concentration risk: Star Trek was already load-bearing in `walking-your-talk.md` (First Officer, Kirk) — a third lean starts costing authority.
- **Became:** the military flight surgeon — the real system the fiction dramatizes. The commander leads the mission; the surgeon owns the medical call on fitness to fly, under conditions defined in advance. (Claim softened from "rank can't override it" to describing the clearance mechanism, since legal mechanics vary by branch.)

## [2026-07-06] Pre-framed reception | `before-you-facilitate.md`

- **Written:** "The unhappy path is a lot to learn" — opening a section by telling facilitator readers the material is burdensome, one sentence before inviting them to engage with it.
- **Rule broken:** Don't Pre-Frame the Reception (this catch named the anti-pattern; Myron Golden source quote in the guide).
- **Became:** "The unhappy path is its own craft... a distinct skill set, built through its own study and reps" — describes the scope, drops the verdict about the reader's experience of it.

## [2026-07-06] Threatening image on good people | `before-you-facilitate.md` (caught in draft)

- **Written:** "a mob with lanyards" — describing the reader's own untrained staff.
- **Rule broken:** Don't Repeat Fiction (the metaphor branch): vivid, but it installs a mob image on the very people the reader trusts. Same failure as repeating "hungry dog" four times about staff.
- **Became:** the mechanism — "the first accusation gets handled by whoever in the room feels most certain," linked to the five dangers of certainty.

## [2026-07-05] Pre-framed reception | `walking-your-talk.md`

- **Written:** invitation script offering "the uncomfortable kind of feedback" — predicting the listener's feeling before delivering the content.
- **Rule broken:** Don't Pre-Frame the Reception (this was the precedent catch, before the rule had a name).
- **Became:** "Are you open to something that might challenge you?" — "challenge" describes what the content does; "uncomfortable" prescribed a feeling.

## [2026-07-05 or earlier] Structure narration | `when-youve-been-wronged.md`

- **Written:** a punchy section close ("you have to act *now*. Here's how to handle that moment.") followed by "(Everything from Afterward on is for once you're out of it.)"
- **Rule broken:** Don't Narrate the Structure. The parenthetical restated what the section title already says, and diluted the close. AI co-authors produce this reflexively.
- **Became:** cut the parenthetical.

## [2026-07-02] Telling, not showing | `trauma-and-filters.md`

- **Written:** "Your Body Tilts the Story" placed in the chapter's model-building zone, opening with abstract mechanism.
- **Rule broken:** Show, Don't Tell — author review: "feels out of place, telling not showing."
- **Became:** relocated to the priming cluster with a show-first opening (the 1 a.m. fight that dissolves at breakfast; the hangry coworker day), so the reader meets the phenomenon before the mechanism.
