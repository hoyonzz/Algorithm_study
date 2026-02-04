import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
box = []

queue = deque()

for i in range(n):
    row = list(map(int, input().split()))
    box.append(row)
    for j in range(m):
        if row[j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                queue.append((nx, ny))
                box[nx][ny] = box[x][y] + 1

result = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
        result = max(result, box[i][j])

print(result - 1)