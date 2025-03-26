from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    def bfs(start_node):
        queue = deque([start_node])
        visited[start_node] = True
        while queue:
            network = queue.popleft()
            for i in range(n):
                if computers[network][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer
