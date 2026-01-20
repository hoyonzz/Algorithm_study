from collections import deque
import sys


input = sys.stdin.readline



n, k = map(int, input().split())
dist = [0] * 100001

def BFS():
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            return dist[x]
        for nx in (x-1, x+1, x*2):
            if 0<= nx <= 100000 and dist[nx]==0:
                dist[nx] = dist[x] + 1
                queue.append(nx)

print(BFS())