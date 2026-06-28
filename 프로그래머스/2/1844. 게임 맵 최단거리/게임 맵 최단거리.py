def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    from collections import deque
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
    bfs(0,0)

    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]