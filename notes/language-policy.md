# Language Policy

This book uses **inarguable language**—descriptions that anyone on any side of an incident could read without feeling attacked or mischaracterized.

## Why This Matters

The words we use affect how we see the world. If your vocabulary only contains victim-frame terms, you can only think about experiences through a victim lens. Words are spells. Don't hex yourself small.

**Language reveals where you are in the healing process:**

| Still Wounded | Healed Equivalent |
|---------------|-------------------|
| "I was violated" | "They crossed my boundaries" |
| "character assassination" | "They attacked my reputation publicly" |
| "witch hunt" | "coordinated attack" |
| "I was banished" | "I was asked to leave" |

---

## REMOVE — Never Use in Author Voice

These terms should **never** appear in the author's voice. They may appear in quotes/examples of what others say.

| Term | Replace With | Why |
|------|--------------|-----|
| character assassination | attacked reputation publicly, reputation attack | "Assassination" is dramatic/victim-frame |
| violated | crossed boundaries, touched without consent, harmed | Judgment wrapped in description |
| witch hunt | coordinated attack, pile-on, accusation cascade | Implies attackers are irrational |
| banished | excluded, removed, asked to leave | Dramatic/medieval; implies righteous exile |

---

## CONTEXT-DEPENDENT — Always Review

These terms are legitimate in some contexts (Drama Triangle framework, quotes, discussing the concept) but problematic in others. **Always flag for review.**

| Term | Okay When | Problematic When |
|------|-----------|------------------|
| victim | Drama Triangle framework, "feeling like a victim" | Used as identity label for a person |
| predator | Quoting what someone called another, discussing the accusation | Used as author's label for a person |
| abuser | Describing established pattern of behavior | Used as character label without evidence |

---

## ALWAYS FINE — No Need to Flag

These terms are neutral and never need review.

| Term | Why Fine |
|------|----------|
| mistake | Neutral description |
| harm | Describes outcome, not character |
| crossed boundaries | Describes action |
| without consent | Describes action |
| attacked | Describes action, not character |
| disproportionate | Describes proportionality |
| over-response | Describes proportionality |

---

## Exceptions

- **Quotes/examples**: People in examples may use moralizing language because real people do.
- **Discussing the concept**: We can discuss what "character assassination" means when explaining why we don't use the term.
- **Drama Triangle terms**: "Victim," "Persecutor," "Rescuer" are acceptable when discussing the Drama Triangle framework specifically.

---

## Automated Checking

See:
- [`language-terms.yaml`](language-terms.yaml) — machine-readable list of flagged terms
- [`language-approved.yaml`](language-approved.yaml) — approved instances with context
- [`../scripts/check_language.py`](../scripts/check_language.py) — checker script

Run: `python scripts/check_language.py`

Output shows unapproved instances as `file:line: term — "context"` (Ctrl+clickable).
