a, r, n = map(int, input().split())

if n == 1:
    print(a)
else:
    print(a * (r ** (n-1)))