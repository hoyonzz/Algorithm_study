def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def DFS(v, n, computers, visited):
        visited[v] = True
        
        # 현재 컴퓨터와 연결된 다른 모든 컴퓨트 확인
        for i in range(n):
            if computers[v][i] == 1 and not visited[i]:
                DFS(i, n, computers, visited)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            DFS(i, n, computers, visited)
    return answer