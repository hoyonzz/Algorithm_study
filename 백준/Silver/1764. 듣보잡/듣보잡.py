import sys
input = sys.stdin.readline

from collections import Counter

n, m = map(int, input().split())
roster_a = []
roster_b = []

for _ in range(n):
    roster_a.append(input())

for _ in range(m):
    roster_b.append(input())

counter_roster_a = Counter(roster_a)
counter_rotser_b = Counter(roster_b)

result = counter_roster_a & counter_rotser_b

result = sorted(result)

print(len(result))
for x in result:
    print(x.strip())