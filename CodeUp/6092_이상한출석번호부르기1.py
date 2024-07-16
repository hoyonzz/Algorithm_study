n = int(input())
arr = list(map(int, input().split()))
d = [0]*23

for i in arr:
    d[i-1] += 1

for i in d:
    print(i, end=' ')