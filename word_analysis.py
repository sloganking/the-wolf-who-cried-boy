"""
Word frequency analysis: compares word usage in this book against
normal English frequency baselines (via the wordfreq library).

Usage:
    python word_analysis.py [--min-count N] [--min-length N] [--top N]

Requirements:
    pip install wordfreq
"""

import os
import re
import argparse
from collections import Counter
from wordfreq import word_frequency

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")


def load_book_text(src_dir):
    all_text = []
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if f.endswith(".md"):
                with open(os.path.join(root, f), "r", encoding="utf-8") as fh:
                    all_text.append(fh.read())

    text = " ".join(all_text)
    text = re.sub(r'\[([^\]]*)\]\([^\)]*\)', r'\1', text)  # strip markdown links
    text = re.sub(r'[#*>`|_\-\[\](){}]', ' ', text)        # strip markdown syntax
    text = re.sub(r'https?://\S+', '', text)                # strip URLs
    return re.findall(r"[a-z']+", text.lower())


def analyze(words, min_count=5, min_length=3, top=None):
    book_counts = Counter(words)
    total_book_words = sum(book_counts.values())

    print(f"Total words in book: {total_book_words}")
    print(f"Unique words: {len(book_counts)}")
    print()

    ratios = []
    for word, count in book_counts.items():
        if count < min_count or len(word) < min_length:
            continue
        book_freq = count / total_book_words
        english_freq = word_frequency(word, 'en')
        if english_freq > 0:
            ratio = book_freq / english_freq
            ratios.append((word, count, book_freq, english_freq, ratio))

    ratios.sort(key=lambda x: x[4], reverse=True)

    if top:
        ratios = ratios[:top]

    print(f"{'WORD':<25} {'COUNT':>6}  {'BOOK FREQ':>10}  {'ENGLISH FREQ':>12}  {'RATIO':>8}")
    print("=" * 75)
    for word, count, bf, ef, ratio in ratios:
        print(f"{word:<25} {count:>6}  {bf:>10.6f}  {ef:>12.8f}  {ratio:>8.1f}x")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze word frequency vs normal English")
    parser.add_argument("--min-count", type=int, default=5, help="Minimum word occurrences (default: 5)")
    parser.add_argument("--min-length", type=int, default=3, help="Minimum word length (default: 3)")
    parser.add_argument("--top", type=int, default=None, help="Show only top N results (default: all)")
    args = parser.parse_args()

    words = load_book_text(SRC_DIR)
    analyze(words, min_count=args.min_count, min_length=args.min_length, top=args.top)
