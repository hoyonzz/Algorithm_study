import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    row = list(map(int, input().strip()))
    maps.append(row)
    
def BFS(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

BFS(0, 0)
print(maps[n-1][m-1])