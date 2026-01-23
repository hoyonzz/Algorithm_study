import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = 0

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
visited = [False]*(n+1)

def DFS(v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i, visited)

    
for i in range(1, n+1):
    if not visited[i]:
        result += 1
        DFS(i, visited)
        
print(result)