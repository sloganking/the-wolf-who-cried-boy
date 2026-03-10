"""
Estimate time spent working on this repo based on git commit timestamps.

Method: Groups commits into "sessions" — if two consecutive commits are
less than `gap_minutes` apart, they're in the same session. Each session's
duration is (last commit - first commit) + a fixed startup buffer.

Usage:
    python time_estimate.py [--gap 120] [--startup 30] [--today]
"""

import subprocess
import argparse
from datetime import datetime, timedelta
from collections import defaultdict


def get_commits():
    result = subprocess.run(
        ["git", "log", "--format=%ai", "--reverse"],
        capture_output=True, text=True, cwd="."
    )
    timestamps = []
    for line in result.stdout.strip().split("\n"):
        if line.strip():
            dt = datetime.fromisoformat(line.strip())
            timestamps.append(dt)
    return timestamps


def estimate_time(timestamps, gap_minutes=120, startup_minutes=30):
    if not timestamps:
        return [], timedelta()

    sessions = []
    session_start = timestamps[0]
    session_end = timestamps[0]

    for i in range(1, len(timestamps)):
        diff = timestamps[i] - timestamps[i - 1]
        if diff.total_seconds() > gap_minutes * 60:
            sessions.append((session_start, session_end))
            session_start = timestamps[i]
        session_end = timestamps[i]

    sessions.append((session_start, session_end))

    total = timedelta()
    startup = timedelta(minutes=startup_minutes)
    for start, end in sessions:
        duration = (end - start) + startup
        total += duration

    return sessions, total


def format_duration(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours}h {minutes}m"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimate time spent on repo")
    parser.add_argument("--gap", type=int, default=120, help="Max minutes between commits in same session (default: 120)")
    parser.add_argument("--startup", type=int, default=30, help="Minutes added per session for startup time (default: 30)")
    parser.add_argument("--today", action="store_true", help="Show only today's work")
    parser.add_argument("--by-day", action="store_true", help="Show breakdown by day")
    args = parser.parse_args()

    timestamps = get_commits()

    if not timestamps:
        print("No commits found.")
        exit()

    print(f"Total commits: {len(timestamps)}")
    print(f"First commit: {timestamps[0].strftime('%Y-%m-%d %H:%M')}")
    print(f"Latest commit: {timestamps[-1].strftime('%Y-%m-%d %H:%M')}")
    print(f"Session gap: {args.gap} min | Startup buffer: {args.startup} min")
    print()

    if args.today:
        today = datetime.now().date()
        timestamps = [t for t in timestamps if t.date() == today]
        if not timestamps:
            print("No commits today.")
            exit()
        sessions, total = estimate_time(timestamps, args.gap, args.startup)
        print(f"Today ({today}):")
        print(f"  Commits: {len(timestamps)}")
        print(f"  Sessions: {len(sessions)}")
        print(f"  Estimated time: {format_duration(total)}")
        for i, (start, end) in enumerate(sessions):
            dur = (end - start) + timedelta(minutes=args.startup)
            print(f"    Session {i+1}: {start.strftime('%H:%M')} - {end.strftime('%H:%M')} ({format_duration(dur)})")
    elif args.by_day:
        by_day = defaultdict(list)
        for t in timestamps:
            by_day[t.date()].append(t)

        grand_total = timedelta()
        for day in sorted(by_day.keys()):
            day_timestamps = by_day[day]
            sessions, total = estimate_time(day_timestamps, args.gap, args.startup)
            grand_total += total
            print(f"  {day}  |  {len(day_timestamps):>3} commits  |  {len(sessions)} sessions  |  {format_duration(total):>8}")

        print()
        print(f"  TOTAL: {format_duration(grand_total)}")
    else:
        sessions, total = estimate_time(timestamps, args.gap, args.startup)
        print(f"Total sessions: {len(sessions)}")
        print(f"Estimated total time: {format_duration(total)}")
