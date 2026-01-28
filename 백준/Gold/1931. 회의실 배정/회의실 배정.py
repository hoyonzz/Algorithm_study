import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))
    
t = 0
result = 0

sorted_meetings = sorted(meetings, key=lambda x:(x[1], x[0]))

for s, e in sorted_meetings:
    if t <= s:
        result += 1
        t = e

print(result)