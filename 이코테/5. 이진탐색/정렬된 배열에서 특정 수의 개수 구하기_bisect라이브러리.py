from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

print(bisect_right(arr, x) - bisect_left(arr, x))