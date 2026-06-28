def solution(n, computers):
    visited = [False] * n
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if computers[v][i] == 1 and not visited[i]:
                dfs(i)

    answer = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer