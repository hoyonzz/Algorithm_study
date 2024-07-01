import sys

input = sys.stdin.readline

n, k = map(int, input().split())

answer = 0

while True:
    target = n // k * k
    answer += n - target
    n = target

    if n < k:
        break

    answer += 1
    n = n // k

answer += n - 1
print(answer)
