import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, devide = map(int, input().split())

total = nums[0]
max_value, min_value = -int(1e9), int(1e9)

def backtracking(idx, total, plus, minus, multiply, devide):
    global max_value, min_value
    if idx == n:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return
    
    if plus > 0:
        backtracking(idx+1, total+nums[idx], plus-1, minus, multiply, devide)

    if minus > 0:
        backtracking(idx+1, total-nums[idx], plus, minus-1, multiply, devide)
    
    if multiply > 0:
        backtracking(idx+1, total*nums[idx], plus, minus, multiply-1, devide)

    if devide > 0:
        backtracking(idx+1, int(total / nums[idx]), plus, minus, multiply, devide-1)

    
backtracking(1, total, plus, minus, multiply, devide)
print(max_value)
print(min_value)
