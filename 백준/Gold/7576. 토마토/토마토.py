import sys
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())
board = []

queue = deque()

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
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
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

answer = 0 

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit()
        answer = max(answer, board[i][j])

print(answer-1)