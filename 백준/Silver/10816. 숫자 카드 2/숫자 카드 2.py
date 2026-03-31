import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dict_nums = {}
for i in range(n):
    if nums[i] in dict_nums:
        dict_nums[nums[i]] += 1
    else:
        dict_nums[nums[i]] = 1

m = int(input())
target = list(map(int, input().split()))

for i in range(m):
    print(dict_nums.get(target[i], 0), end = ' ')

