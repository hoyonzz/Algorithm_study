n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for i in range(n):
    if arr[i] < x:
        result.append(arr[i])

for i in result:
    print(i, end=' ')