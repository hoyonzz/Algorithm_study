from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0))
    while queue:
        r, c = queue.popleft()
        if r == rows -1 and c == cols -1:
            return maps[r][c]
        
        # 4가지 방향 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols:
                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    queue.append((nr,nc))
    return -1
    
