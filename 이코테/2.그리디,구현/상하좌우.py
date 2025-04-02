n = int(input())
commands = list(input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D']
x, y = 0, 0

for command in commands:
    for i in range(4):
        if command == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break
    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny

print(x+1, y+1)