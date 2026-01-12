# 준비
import sys
from collections import deque


input = sys.stdin.readline



dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


# 함수 정의
def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if not visited[nx][ny] and maps[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

# while 반복문
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    maps = []
    result = 0
    for _ in range(h):
        row = list(map(int, input().split()))
        maps.append(row)
    visited = [[False] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] == 1:
                BFS(i, j)
                result += 1
    print(result)


    