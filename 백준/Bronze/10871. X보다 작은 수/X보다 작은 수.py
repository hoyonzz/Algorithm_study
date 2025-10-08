n, x = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

for i in range(n):
    if arr[i] < x:
        answer.append(arr[i])

for i in answer:
    print(i, end=' ')