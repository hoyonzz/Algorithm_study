a, b, c  = map(int, input().split())
print((b if b<c else c) if ((b if b<c else c)<a) else a)
