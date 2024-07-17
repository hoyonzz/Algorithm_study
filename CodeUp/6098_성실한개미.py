map = []
for _ in range(10):
    row = list (map (int, input().split()))
    map.append(row)
    
nx, ny = 1, 1
dx = [0, 1]
dy = [1, 0]

while True:
    # 먹이를 발견한 경우
    if map[nx][ny] == 2:
        map[nx][ny] = 9
        break
    
    # 벽인 경우
    if map[nx][ny] == 1:
        # 아래로 이동할 수 있는 경우
        if map[nx+1][ny] == 0:
            nx, ny = nx+1, ny
        # 아래도 이동할 수 없는 경우
        else: break
    
    # 이동
    if map[nx][ny] == 0:
        map[nx][ny] = 9
        nx, ny = nx, ny+1

for i in range(10):
    for j in range(10):
        print(map[i][j], end = ' ')
    print()