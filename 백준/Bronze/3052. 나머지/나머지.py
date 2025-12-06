import sys
input = sys.stdin.readline
mods = [0] * 42
for _ in range(10):
    mods[int(input())%42]+=1
result = 0
for i in range(len(mods)):
    if mods[i] >= 1:
        result += 1
print(result)