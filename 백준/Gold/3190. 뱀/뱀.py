import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2
l = int(input())
move_plans = {}
for _ in range(l):
    x, c = input().split()
    move_plans[int(x)] = c
result = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 1
snake = deque([(0, 0)])
x, y = 0, 0
board[0][0] = 1

while True:
    result += 1
    
    nx = x + dx[(d-1)%4]
    ny = y + dy[(d-1)%4]
    
    if not(0<=nx<n and 0<=ny<n) or board[nx][ny] == 1:
        break
        
    snake.append((nx, ny))
    
    if board[nx][ny] == 2:
        # 사과가 있다면, 사과쪽엔 머리가, 몸길이 늘어남
        board[nx][ny] = 1
    else:
        # 사과가 없다면, 몸길이 줄어들고 이동
        tx, ty = snake.popleft()
        board[tx][ty] = 0
        board[nx][ny] = 1
             
    x, y = nx, ny
    
    if result in move_plans:
        if move_plans[result] == 'D':
            d += 1
        else:
            d -= 1
            
print(result)
        