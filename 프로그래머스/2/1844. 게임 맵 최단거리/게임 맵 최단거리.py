def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    def bfs(x, y):
        from collections import deque
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < n and 0<= ny < m:
                    if maps[nx][ny] == 1:
                        maps[nx][ny] = maps[x][y] + 1
                        queue.append((nx, ny))
                        
    bfs(0, 0)
    
    if maps[n-1][m-1] <= 1:
        return -1
    return maps[n-1][m-1]