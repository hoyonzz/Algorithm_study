n = int(input())

d = [ [0] * 19 for _ in range(19)]

for _ in range(n):
    x, y = map(int, input().split())
    if d[x-1][y-1] == 0:
        d[x-1][y-1] += 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')

    print()