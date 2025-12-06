import sys
input = sys.stdin.readline

arr = [0] + [1]*30

for _ in range(28):
    n = int(input())
    arr[n] = 0
    
for i in range(1, 31):
    if arr[i] == 1:
        print(i)