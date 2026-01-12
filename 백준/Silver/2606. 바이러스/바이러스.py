import sys

input = sys.stdin.readline



n = int(input())
m = int(input())
computers = [[] for _ in range(n+1)]
visited = [0] * (n+1)


for _ in range(m):
    s, e = map(int, input().split())
    computers[s].append(e)
    computers[e].append(s)
    
def DFS(v):
    visited[v] = True
    for i in computers[v]:
        if not visited[i]:
            DFS(i)

DFS(1)
print(visited.count(1)-1)
