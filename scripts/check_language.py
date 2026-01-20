#!/usr/bin/env python3
"""
Language Checker for Responsible Play

Scans src/ and drafts/ for moralizing terms and reports unapproved instances.
Output is file:line format (Ctrl+clickable in most editors).

Usage:
    python scripts/check_language.py

Exit codes:
    0 - All instances approved (or no instances found)
    1 - Unapproved instances found
"""

import os
import re
import sys
from pathlib import Path
from typing import NamedTuple

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Try to import yaml, provide helpful error if missing
try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)


class Match(NamedTuple):
    """A single match of a flagged term."""
    file: str
    line_num: int
    term: str
    line_content: str


class ApprovedInstance(NamedTuple):
    """An approved instance from the YAML file."""
    term: str
    file: str
    context: str
    reason: str


def load_terms(terms_path: Path) -> list[str]:
    """Load all flagged terms from the terms YAML file."""
    with open(terms_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    terms = []
    if data.get('remove_always'):
        terms.extend(data['remove_always'])
    if data.get('context_dependent'):
        terms.extend(data['context_dependent'])
    
    return terms


def load_approved(approved_path: Path) -> list[ApprovedInstance]:
    """Load approved instances from the approved YAML file."""
    if not approved_path.exists():
        return []
    
    with open(approved_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    if not data or not data.get('approved'):
        return []
    
    instances = []
    for item in data['approved']:
        if item is None:
            continue
        instances.append(ApprovedInstance(
            term=item.get('term', ''),
            file=item.get('file', ''),
            context=item.get('context', ''),
            reason=item.get('reason', '')
        ))
    
    return instances


def find_matches(search_dirs: list[Path], terms: list[str]) -> list[Match]:
    """Find all occurrences of flagged terms in the given directories."""
    matches = []
    
    for search_dir in search_dirs:
        if not search_dir.exists():
            continue
        
        for md_file in search_dir.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
            except Exception as e:
                print(f"Warning: Could not read {md_file}: {e}", file=sys.stderr)
                continue
            
            for line_num, line in enumerate(lines, start=1):
                line_lower = line.lower()
                for term in terms:
                    # Case-insensitive search
                    if term.lower() in line_lower:
                        # Get relative path for cleaner output
                        try:
                            rel_path = md_file.relative_to(Path.cwd())
                        except ValueError:
                            rel_path = md_file
                        
                        matches.append(Match(
                            file=str(rel_path),
                            line_num=line_num,
                            term=term,
                            line_content=line.strip()
                        ))
    
    return matches


def is_approved(match: Match, approved: list[ApprovedInstance]) -> bool:
    """Check if a match is in the approved list."""
    for instance in approved:
        # Normalize paths for comparison
        match_file = match.file.replace('\\', '/')
        instance_file = instance.file.replace('\\', '/')
        
        if (instance.term.lower() == match.term.lower() and
            instance_file in match_file and
            instance.context.lower() in match.line_content.lower()):
            return True
    
    return False


def truncate_context(line: str, term: str, max_len: int = 60) -> str:
    """Truncate line content to show context around the term."""
    # Find term position (case-insensitive)
    lower_line = line.lower()
    lower_term = term.lower()
    pos = lower_line.find(lower_term)
    
    if pos == -1:
        # Term not found (shouldn't happen), just truncate
        return line[:max_len] + "..." if len(line) > max_len else line
    
    # Show context around the term
    start = max(0, pos - 20)
    end = min(len(line), pos + len(term) + 20)
    
    result = line[start:end]
    if start > 0:
        result = "..." + result
    if end < len(line):
        result = result + "..."
    
    return result


def main():
    # Find project root (where this script lives in scripts/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Paths
    terms_path = project_root / 'notes' / 'language-terms.yaml'
    approved_path = project_root / 'notes' / 'language-approved.yaml'
    search_dirs = [
        project_root / 'src',
        project_root / 'drafts'
    ]
    
    # Validate paths
    if not terms_path.exists():
        print(f"Error: Terms file not found: {terms_path}")
        sys.exit(1)
    
    # Load data
    terms = load_terms(terms_path)
    approved = load_approved(approved_path)
    
    print(f"Checking for {len(terms)} flagged terms...")
    print(f"Loaded {len(approved)} approved instances.\n")
    
    # Find matches
    matches = find_matches(search_dirs, terms)
    
    # Filter to unapproved
    unapproved = [m for m in matches if not is_approved(m, approved)]
    
    if not unapproved:
        print("All instances approved (or no flagged terms found).")
        sys.exit(0)
    
    # Report unapproved
    print(f"Found {len(unapproved)} unapproved instance(s):\n")
    
    # Group by file for cleaner output
    by_file: dict[str, list[Match]] = {}
    for match in unapproved:
        by_file.setdefault(match.file, []).append(match)
    
    for file_path, file_matches in sorted(by_file.items()):
        for match in sorted(file_matches, key=lambda m: m.line_num):
            context = truncate_context(match.line_content, match.term)
            print(f"{match.file}:{match.line_num}: {match.term}")
            print(f"    \"{context}\"\n")
    
    print(f"\nTotal: {len(unapproved)} unapproved instance(s)")
    print("\nTo approve an instance, add it to notes/language-approved.yaml")
    
    sys.exit(1)


if __name__ == '__main__':
    main()
