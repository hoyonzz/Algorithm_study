import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    point_tuple = tuple(map(int, input().split()))
    arr.append(point_tuple)
arr.sort()
for i in range(n):
    print(arr[i][0],arr[i][1])