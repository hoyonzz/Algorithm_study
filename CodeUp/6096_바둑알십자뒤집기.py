d = []

for _ in range(19):
    row = list(map(int, input().split()))
    d.append(row)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    
    for i in range(19):
        if d[x][i] == 0:
            d[x][i] = 1
        else:
            d[x][i] = 0
    
    for i in range(19):
        if d[i][y] == 0:
            d[i][y] = 1
        else:
            d[i][y] = 0

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()
