n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
answer = 0
sum_arr = sum(arr)

answer = sum_arr / m * 100 / n

print(answer)
