from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0]*101 for _ in range(102)]
    # 직사각형 그리기
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1*2, y2*2 +1):
            for x in range(x1*2, x2*2 +1):
                board[y][x] = 1
    
    # 테두리만 남기기
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1*2+1, y2*2):
            for x in range(x1*2+1, x2*2):
                board[y][x] = 0
    
    # 방향벡터 선언
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    # 큐 생성
    queue = deque()
    queue.append(((characterY*2),(characterX*2)))
    
    # BFS탐색
    while queue:
        y, x = queue.popleft()
        # 종료조건 명시
        if y == (itemY*2) and x == (itemX*2):
            return board[y][x] // 2
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > 100 or ny > 100:
                continue
            if board[ny][nx] == 1:
                board[ny][nx] = board[y][x] + 1
                queue.append((ny, nx))
    return board[itemY*2][itemX*2]//2
