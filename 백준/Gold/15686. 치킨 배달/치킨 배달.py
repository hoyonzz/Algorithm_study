import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

chicken_houses = []
houses = []
selected = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 2:
            chicken_houses.append((i+1, j+1))
        elif row[j] == 1:
            houses.append((i+1, j+1))

# 집마다 치킨거리를 구하는 함수
def get_chicken_dist():
    total_dist = 0
    # 집들은 고정
    for i in range(len(houses)):
        hr, hc = houses[i]
        min_chicken_dist = float('inf')
        for cr, cc in selected:
            dist = abs(hr-cr) + abs(hc-cc)
            min_chicken_dist = min(min_chicken_dist, dist)
        total_dist += min_chicken_dist
    return total_dist

result = float('inf')
# 백트레킹 함수
def backtracking(idx, count):
    global result
    # 종료조건
    if count == m:
        result = min(result, get_chicken_dist())
        return
    
    # 치킨집 순회(백트레킹)
    for i in range(idx, len(chicken_houses)):
        selected.append(chicken_houses[i])

        backtracking(i+1, count+1)

        selected.pop()

backtracking(0, 0)

print(result)