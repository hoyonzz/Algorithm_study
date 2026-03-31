import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_value = float('-inf')
min_value = float('inf')

def backtracking(depth, total, plus, minus, mul, div):
    global max_value, min_value
    if depth == n:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return
    if plus > 0:
        backtracking(depth + 1, total + nums[depth], plus - 1, minus, mul, div)
    if minus > 0:
        backtracking(depth + 1, total - nums[depth], plus, minus - 1, mul, div)
    if mul > 0:
        backtracking(depth + 1, total * nums[depth], plus, minus, mul - 1, div)
    if div > 0:
        backtracking(depth + 1, int(total / nums[depth]), plus, minus, mul, div - 1)

backtracking(1, nums[0], plus, minus, mul, div)

print(max_value)
print(min_value)