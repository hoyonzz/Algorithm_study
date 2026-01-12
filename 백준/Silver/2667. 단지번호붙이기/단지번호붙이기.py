from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
maps = []
for _ in range(n):
    row = list(map(int, input().strip()))
    maps.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

visited = [[0] * n for _ in range(n)]

def BFS(x, y):
    count = 1
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1

                if maps[nx][ny] == 1:
                    count += 1
                    queue.append((nx, ny))
    return count

for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == 1:
            result.append(BFS(i, j))

print(len(result))
result.sort()
for i in result:
    print(i)
                    
                