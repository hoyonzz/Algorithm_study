import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
board = []

for _ in range(n):
    row = list(map(int, input().strip()))
    board.append(row)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and board[nx][ny] == 1:
                dfs(nx, ny)

result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)
            
result.sort()

print(len(result))
for i in result:
    print(i)