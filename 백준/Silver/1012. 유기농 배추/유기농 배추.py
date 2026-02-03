import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and board[nx][ny] ==1 :
                dfs(nx, ny)
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1
        
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == 1:
                dfs(i, j)
                result += 1
                
    print(result)