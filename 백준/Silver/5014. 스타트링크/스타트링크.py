from collections import deque
import sys

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

count = [0] * (f+1)

def BFS():
    queue = deque([s])
    count[s] = 1
    while queue:
        x = queue.popleft()
        if x == g:
            return count[x]-1
        for nx in (x-d, x+u):
            if 0 < nx <= f and count[nx] == 0:
                count[nx] = count[x] + 1
                queue.append(nx)

    return "use the stairs"

print(BFS())
    