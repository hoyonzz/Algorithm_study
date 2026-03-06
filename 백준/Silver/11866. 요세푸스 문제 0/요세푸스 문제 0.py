import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

queue = deque([x for x in range(1, n+1)])
result = []
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result))+">")