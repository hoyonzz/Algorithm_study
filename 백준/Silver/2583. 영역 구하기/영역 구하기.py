import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1
        

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    if x < 0 or y < 0 or x >= m or y >= n or graph[x][y] == 1:
        return 0
    
    graph[x][y] = 1
    
    area = 1
    for i in range(4):
        area += DFS(x + dx[i], y + dy[i])
        
    return area

result = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(DFS(i, j))
           
        
print(len(result))
result.sort()
for i in result:
    print(i, end = ' ')
        
    
        