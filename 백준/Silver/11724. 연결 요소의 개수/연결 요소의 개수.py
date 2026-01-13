import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)



result = 0

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

for i in range(1, n+1):
    if not visited[i]:
        DFS(i)
        result += 1
        
print(result)