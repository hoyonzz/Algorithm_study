import sys
from collections import deque


input = sys.stdin.readline



n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n+1):
    graph[i].sort()

def DFS(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
visited = [0] * (n+1)
DFS(v)
print()
visited = [0] * (n+1)
BFS(v)
                