import sys

input = sys.stdin.readline


r, c = map(int, input().split())
graph = []

for _ in range(r):
    rows = list(input().strip())
    graph.append(rows)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS():
    # 정답 변수 최소 한칸
    answer = 1
    
    # 초기 상태
    q = set([(0, 0, graph[0][0])])



    while q:
        next_q = set()
    
        for x, y, path in q:
            # 정답 갱신
            answer = max(answer, len(path))
        
            # 방향 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                # 범위 체크
                if 0<=nx<r and 0<=ny<c:
                    #중복 알파벳 체크
                    if graph[nx][ny] not in path:
                        next_q.add((nx, ny, path+graph[nx][ny]))
                    
        q = next_q
        
    return answer

print(BFS())