def solution(n, computers):
    visited = [False] * n
    answer = 0 
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if not visited[i] and computers[v][i] == 1:
                dfs(i)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer