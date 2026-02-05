import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = []

def backtracking(depth, start):
    # 개수가 맞으면 출력 후 반환
    if depth == m:
        print(*result)
        return
    
    # n까지 수 체크(자기자신포함!)
    for i in range(start, n+1):
        result.append(i)
        backtracking(depth+1, i)

        result.pop()

backtracking(0, 1)