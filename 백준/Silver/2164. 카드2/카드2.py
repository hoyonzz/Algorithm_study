import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
queue = deque([x for x in range(1, n+1)])

while True:
    if len(queue) <= 1:
        break
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

    