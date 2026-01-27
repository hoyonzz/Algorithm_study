import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = [arr[0]]


for i in range(1, n):
    result.append(result[i-1]+arr[i])
    
print(sum(result))
    

    