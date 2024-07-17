h, w = map(int, input().split())
board = [ [0]*w for _ in range(h)]
n = int(input())
for _ in range(n):
    i, d, x, y = map(int, input().split())
    x, y = x-1, y-1
    if d == 0:
        for j in range(i):
            board[x][y+j] = 1
    else:
        for j in range(i):
            board[x+j][y] = 1

for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    print()