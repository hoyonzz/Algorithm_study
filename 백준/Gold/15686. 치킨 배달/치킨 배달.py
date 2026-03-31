import sys
input = sys.stdin.readline

houses = []
chicken_houses = []
selected_houses = []

n, m = map(int, input().split())

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            houses.append((i, j))
        if row[j] == 2:
            chicken_houses.append((i, j))


answer = float('inf')

def backtracking(idx):
    global answer
    if len(selected_houses) == m:
        chicken_distance = 0
        for r1, c1 in houses:
            distance = float('inf')
            for r2, c2 in selected_houses:
                distance = min(distance, (abs(r1-r2) + abs(c1-c2)))
            chicken_distance += distance
        answer = min(answer, chicken_distance)
        return
    
    for i in range(idx, len(chicken_houses)):
        selected_houses.append(chicken_houses[i])
        backtracking(i + 1)
        selected_houses.pop()

backtracking(0)

print(answer)
