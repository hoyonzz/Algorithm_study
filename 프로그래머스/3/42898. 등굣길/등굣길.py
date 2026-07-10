def solution(m, n, puddles):
    board = [[0]*m for _ in range(n)]

    for i in range(len(puddles)):
        x = puddles[i][1] -1
        y = puddles[i][0] -1
        board[x][y] = -1
        
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                board[i][j] = 1
                continue
            
            if board[i][j] == -1:
                board[i][j] = 0
                continue
                
            up = board[i-1][j] if i > 0 else 0
            left = board[i][j-1] if j > 0 else 0
            
            board[i][j] = (up+left)
            
    return board[n-1][m-1]  % 1000000007
