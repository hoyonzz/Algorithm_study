import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num, s = input().split()
    result = ''
    for char in s:
        result += char * int(num)
    print(result)