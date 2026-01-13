import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] == 1:
            queue.append((i, j))
    
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 0:
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        else:
            result = max(result, graph[i][j])
print(result -1)