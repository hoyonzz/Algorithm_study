import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
maps = []

for _ in range(n):
    row = list(map(int, input().split()))
    maps.append(row)
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

while True:
    if maps[x][y] == 0:
        maps[x][y] = 2
        answer += 1
    is_moved = False
    for i in range(4):
        d = (d-1) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 0:
                x, y = nx, ny
                is_moved = True
                break
    if is_moved:
        continue
    else:
        nx = x - dx[d]
        ny = y - dy[d]
        if maps[nx][ny] == 1:
            break
        x, y = nx, ny

print(answer)