def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = x + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

from collections import deque

# n, m을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 방향 정의 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))
