import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while queue:
    
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if not visited[nx][ny] and graph[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            result.append(BFS(i, j))

if result:
    print(len(result))
    print(max(result))
    
else:
    print(0)
    print(0)
