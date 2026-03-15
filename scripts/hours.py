import subprocess
import datetime

result = subprocess.run(["git", "log", "--format=%ai", "--reverse"], capture_output=True, text=True)
timestamps = []
for line in result.stdout.strip().split("\n"):
    dt = datetime.datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")
    timestamps.append(dt)

SESSION_GAP = 120
FIRST_COMMIT_BONUS = 30

sessions = []
session_start = timestamps[0]
session_commits = 1
total_minutes = FIRST_COMMIT_BONUS

for i in range(1, len(timestamps)):
    gap = (timestamps[i] - timestamps[i - 1]).total_seconds() / 60
    if gap > SESSION_GAP:
        sessions.append((session_start, timestamps[i - 1], session_commits))
        session_start = timestamps[i]
        session_commits = 1
        total_minutes += FIRST_COMMIT_BONUS
    else:
        total_minutes += gap
        session_commits += 1

sessions.append((session_start, timestamps[-1], session_commits))

total_hours = total_minutes / 60
print(f"Total commits: {len(timestamps)}")
print(f"Total sessions: {len(sessions)}")
first = timestamps[0].strftime("%b %d")
last = timestamps[-1].strftime("%b %d, %Y")
print(f"Date range: {first} - {last}")
print(f"Estimated hours: {total_hours:.1f}")
print()
print("Sessions by day:")
day_hours = {}
for s_start, s_end, s_commits in sessions:
    day = s_start.strftime("%b %d")
    dur = (s_end - s_start).total_seconds() / 60 + FIRST_COMMIT_BONUS
    day_hours[day] = day_hours.get(day, 0) + dur

for day, mins in sorted(day_hours.items(), key=lambda x: x[1], reverse=True):
    print(f"  {day}: {mins / 60:.1f}h")
