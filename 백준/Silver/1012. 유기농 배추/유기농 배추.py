from collections import deque

t = int(input())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
    

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]:
                BFS(i, j)
                count += 1
                
    print(count)
    