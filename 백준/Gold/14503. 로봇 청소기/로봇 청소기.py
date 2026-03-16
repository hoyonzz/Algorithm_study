import sys
input = sys.stdin.readline


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

answer = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    # 자리 청소
    if board[r][c] == 0:
        board[r][c] = 2
        answer += 1
    
    # 주변 탐색
    possible_cleaning = False

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if board[nr][nc] == 0:
            possible_cleaning = True
            break
    
    if not possible_cleaning:
        br = r - dr[d]
        bc = c - dc[d]
        if board[br][bc] != 1:
            r, c = br, bc
        else:
            break

    else: # 주변에 청소할 공간이 있다면,
        # 반시계 방향 회전
        d = (d-1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if board[nr][nc] == 0:
            r, c = nr, nc

print(answer)