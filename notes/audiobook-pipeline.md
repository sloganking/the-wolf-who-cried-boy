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

Rust CLI, OpenAI TTS via `async-openai`. Per page: render the page to an image
(ImageMagick), extract the text (`pdftotext`, falling back to `tesseract` OCR),
speak it, then mux audio with the page images into a video.

Flags worth knowing (`src/options.rs`):

| Flag | Why it matters |
|---|---|
| `--pdf <path>` | Point at the copied `book.pdf` |
| `--voice <name>` | 13 OpenAI voices; defaults to `alloy` |
| `--sample 5` | Do this first — cheap 5-page run to confirm nothing's broken before paying for the full render |
| `--audio-only` | Stops after the combined mp3, skipping the slow video encode |
| `--text-overrides <dir>` | Per-page replacement text, `page-NNN.txt`, 0-indexed, zero-padded to 3 digits |
| `--ocr` | Force OCR instead of embedded text extraction |

**Text overrides are the escape hatch for pages that extract as garbage** — ASCII-art
diagrams, tables, anything visual. The last run needed exactly one
(`text_overrides/page-165.txt`, the Fawning Dynamic diagram, rewritten as prose).
Expect to need more as diagrams get added.

## Splitting for YouTube

**YouTube won't accept a file longer than 10 hours**, so the full render gets cut in
half and uploaded as two parts. The split is a plain duration bisect, not a chapter
boundary — part 1 ends wherever the midpoint lands, mid-sentence.

Renders so far:

| Render | Full | Parts |
|---|---|---|
| April 2026 | 13h 35m (48,939 s) | 2 × 6h 48m |
| June 2026 | 15h 55m (57,313 s) | 2 × 7h 57m |

If it's ever worth splitting at a real boundary, [SUMMARY.md](../src/SUMMARY.md) has a
natural one: end part 1 after "The Patterns", open part 2 with "Before You Play" —
the book's own turn from diagnosis to practice.

## Current Length

The June render is **15h 55m**, made from a manuscript of ~159,000 words. That works
out to ~167 wpm, which is the number to reuse for estimates.

The manuscript is now ~180,700 words, so a fresh render would run **~18 hours** — about
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
- **Always `--sample 5` first.** A full run is 18 hours of paid TTS.
