import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = []

def backtracking(depth, start):
    if depth == m:
        print(*result)
        return
    
    for i in range(start, n+1):
        result.append(i)
        
        backtracking(depth+1, i+1)

        result.pop()


backtracking(0, 1)