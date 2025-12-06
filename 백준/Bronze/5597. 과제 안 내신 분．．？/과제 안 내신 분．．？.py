import sys
input = sys.stdin.readline

arr = {i for i in range(1, 31)}
check = set()
for _ in range(28):
    check.add(int(input()))

print(*sorted(arr-check), sep='\n')