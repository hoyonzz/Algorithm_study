import sys

input = sys.stdin.readline

n = int(input())
answer = 0


for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) or "3" in str(m) or "3" in str(s):
                answer += 1


print(answer)
