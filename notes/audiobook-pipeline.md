# Audiobook Pipeline

How the audiobook gets made. The tooling does **not** live in this repo — it's a
separate Rust CLI in a sibling directory.

## The Chain

```
src/*.md  →  mdbook  →  book.pdf  →  audiobook-creator  →  .mp3 / .mp4
```

1. **This repo renders the PDF.** `mdbook build` with the `[output.pdf]` block in
   [book.toml](../book.toml) uncommented, then copy `docs/pdf/output.pdf` to
   `book.pdf` and re-comment the block. (It stays commented because it splits the
   build into `docs/html/` and `docs/pdf/`, which breaks `mdbook serve`.)
2. **The other repo turns that PDF into the audiobook.** It reads the PDF, not the
   markdown — so anything that looks wrong in the PDF will sound wrong in the audio.

## The Tool

`../audiobook-creator` — <https://github.com/sloganking/audiobook-creator>

Rust CLI, OpenAI TTS (`tts-1-hd`) via `async-openai`. Per page: extract the text
(`pdftotext`, or `tesseract` OCR), speak it, then mux the audio with page images
(ImageMagick `magick`, else poppler's `pdftoppm`) into a video. `--help` prints the
whole recipe.

**Chapters (since Oct 19, 2026).** The tool reads the PDF's outline (bookmarks; the
mdbook PDF has one, 44 top-level entries in the Oct 19 build) and at each chapter
start:

- **says it:** a short clip, "Chapter: <heading as printed>.", with a brief pause on
  either side. The heading line is removed from the page text so it isn't read twice.
  A heading partway down a page (e.g. "If You Made the Mistake" on p352) splits that
  page's audio at the heading. `--no-announce` turns this off;
- **marks it:** real chapter metadata in both the `.mp3` and the `.mp4`, so players
  show sections;
- **lists it for YouTube:** `<output>.youtube.txt`, `00:00 Title` lines from the
  measured clip durations. A chapter under 10 s is merged into the next; a part with
  fewer than 3 chapters gets no list, because YouTube would ignore it.

With no outline it falls back to "Chapter N" / "Part N" headings, labeled HEURISTIC;
a PDF with neither gets no chapters.

Flags worth knowing (`src/options.rs`):

| Flag | Why it matters |
|---|---|
| `--pdf <path>` | Point at the copied `book.pdf` |
| `--dry-run` | Free: chapter list, character count, cost and duration estimate, projected split. No TTS |
| `--start-page N --sample K` | A cheap paid check of pages N..N+K-1. Pages 351-356 cross three chapter starts |
| `--max-cost <USD>` | A paid run refuses to start above this (default $1), so a full render needs e.g. `--max-cost 40` |
| `--voice <name>` | 13 OpenAI voices; defaults to `alloy` |
| `--audio-only` | Stops after the chaptered mp3, skipping the slow video encode |
| `--text-overrides <dir>` | Per-page replacement text, `page-NNN.txt`, 0-indexed, zero-padded to 3 digits |
| `--ocr` | Force OCR instead of embedded text extraction |

**Every clip is cached** in `./audio`, keyed on its exact text and voice, so a crash
partway through re-pays nothing already spoken. Each paid call's character count goes
to `./audio/tts-ledger.jsonl`.

**Text overrides are the escape hatch for pages that extract as garbage** — ASCII-art
diagrams, tables, anything visual. The last run needed exactly one
(`text_overrides/page-165.txt`, the Fawning Dynamic diagram, rewritten as prose).
Expect to need more as diagrams get added.

## Splitting for YouTube

**YouTube won't accept a file longer than 10 hours**, so a long render becomes parts.
Since Oct 19, 2026 the cut falls **on a chapter start**: the one nearest the even
split that keeps every part under 10 h minus a 15-minute margin (`--max-part-hours`,
`--split-margin-minutes`). Parts are `<output>-part1.mp4`, `-part2.mp4`, and so on.
Each has its own chapter metadata and its own `.youtube.txt`, both restarting at
`00:00`. Only if no set of chapter starts fits does it fall back to a page boundary,
and it prints a warning when it does.

The Oct 19 dry run projects the current manuscript at ~18h 31m in two parts, **part 2
opening with "Appropriate Response"** (~9h 11m in). The real run re-chooses from
measured audio durations. The old suggestion (end part 1 after "The Patterns", open
part 2 with "Before You Play") no longer fits: part 2 would run ~10.6 h, over the cap.

Renders so far (both split with the old plain duration bisect, mid-sentence):

| Render | Full | Parts |
|---|---|---|
| April 2026 | 13h 35m (48,939 s) | 2 × 6h 48m |
| June 2026 | 15h 55m (57,313 s) | 2 × 7h 57m |

## Current Length

The June render is **15h 55m**, made from a manuscript of ~159,000 words. That works
out to ~167 wpm, which is the number to reuse for estimates.

The Oct 19, 2026 PDF has ~186,900 words (the tool's count over the PDF text, which
includes the glossary and quick reference). A 6-page sample measured **168.6 wpm**
(tts-1-hd, alloy). That puts a fresh render at **~18h 31m** and ~1.1M characters,
**~$33** at $30 per 1M characters. Earlier, by manuscript count (~180,700 words), it was **~18 hours** — about
two hours longer than what's currently rendered, and it includes chapters the existing
audio doesn't have at all (e.g. [where-the-police-fit.md](../src/concepts/where-the-police-fit.md),
split out after the June render).

## Gotchas

- **Audio artifacts are gitignored** (`*.mp3`, `*.mp4` in [.gitignore](../.gitignore)).
  The files in `audiobook/`, `audiobook-archive/`, and the `audiobook-latest.*` set are
  untracked local-only — they have no history and won't survive a fresh clone.
- **The PDF in the sibling repo can go stale.** Its copy of
  `the-wolf-who-cried-boy.pdf` is whatever was last dropped there, not a live link to
  this repo's `book.pdf`. Re-copy before every render.
- **Always `--dry-run`, then a small `--sample`, first.** A full run is 18 hours of paid TTS.
