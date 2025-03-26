def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(computer):
        visited[computer] = True
        for i in range(n):
            if visited[i] == 0 and computers[computer][i] == 1:
                dfs(i)
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
            
    return answer