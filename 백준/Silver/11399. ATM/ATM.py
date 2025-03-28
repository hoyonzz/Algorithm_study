n = int(input())
arr = list(map(int, input().split()))
arr.sort()
S= []
tmp = 0
for i in range(n):
    tmp += arr[i]
    S.append(tmp)
print(sum(S))