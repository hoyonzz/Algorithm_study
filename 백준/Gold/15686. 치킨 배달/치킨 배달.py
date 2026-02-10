import sys

input = sys.stdin.readline

n, m = map(int, input().split())
chicken_houses = []
houses = []
selected = []
result = float('inf')

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 2:
            chicken_houses.append((i+1, j+1))
        elif row[j] == 1:
            houses.append((i+1, j+1))

def backtracking(count, idx):
    global result
    if count == m:
        result = min(result, get_chicken_dist())
        return

    for i in range(idx, len(chicken_houses)):
        selected.append(chicken_houses[i])
        backtracking(count+1, i+1)
        selected.pop()

def get_chicken_dist():
    total_dist = 0
    for hr, hc in houses:
        min_dist = float('inf')
        for cr, cc in selected:
            dist = abs(hr-cr) + abs(hc-cc)
            min_dist = min(min_dist, dist)
        total_dist += min_dist
    return total_dist

backtracking(0, 0)
print(result)