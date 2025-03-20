import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left_side = arr[:mid]
    right_side = arr[mid:]
    
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    
    left = right = 0
    merged_arr = []
    
    while left < len(left_side) and right < len(right_side):
        if left_side[left] < right_side[right]:
            merged_arr.append(left_side[left])
            left += 1
        else:
            merged_arr.append(right_side[right])
            right += 1
    if left < len(left_side):
            merged_arr += left_side[left:]
    if right < len(right_side):
            merged_arr += right_side[right:]
    
    return merged_arr

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
    
answer= merge_sort(arr)

for i in range(n):
    print(answer[i])