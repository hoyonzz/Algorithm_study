import sys
from collections import deque


input = sys.stdin.readline



n = int(input())
area = []
max_h = 0
for _ in range(n):
    row = list(map(int, input().split()))
    max_h = max(max_h, max(row))
    area.append(row)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, k, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <=ny < n and area[nx][ny] > k and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1

result = [1]

for h in range(1, max_h):
    visited = [[False] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if area[i][j] > h and not visited[i][j]:
                BFS(i, j, h, visited)
                count += 1
    result.append(count)
    
print(max(result))
                
