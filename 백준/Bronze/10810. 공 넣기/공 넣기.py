import sys
input = sys.stdin.readline
n, m = map(int, input().split())
baskets = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        baskets[l] = k
for i in baskets:
    print(i, end=' ')