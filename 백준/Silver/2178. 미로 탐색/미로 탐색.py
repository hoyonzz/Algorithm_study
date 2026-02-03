import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().strip()))
    board.append(row)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0<=nx<n and 0<=ny<m):
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
bfs(0, 0)
print(board[n-1][m-1])