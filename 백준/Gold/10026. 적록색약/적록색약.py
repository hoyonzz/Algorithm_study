import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
board = []
for _ in range(n):
    row = list(input().strip())
    board.append(row)
    
result = 0
visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and board[nx][ny] == board[x][y]:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result += 1
            
print(result, end=' ')

result = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result += 1

print(result)