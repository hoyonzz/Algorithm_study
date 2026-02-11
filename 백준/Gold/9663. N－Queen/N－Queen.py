import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
answer = 0
visited1 = [0] * n
visited2 = [0] * (2 * n - 1)
visited3 = [0] * (2 * n - 1)

def backtracking(i):
    global answer
    # 종료조건-모든 행이 끝났을 경우
    if i == n:
        answer += 1
        return
    
    for j in range(n):
        # 같은 열에 없어야하고, 대각선이 아니여야함
        if visited1[j] == 0 and visited2[i-j+n-1] == 0 and visited3[i+j] == 0:
            visited1[j] = 1
            visited2[i-j+n-1] = 1
            visited3[i+j] = 1
            backtracking(i+1)

            visited1[j] = 0
            visited2[i-j+n-1] = 0
            visited3[i+j] = 0

backtracking(0)

print(answer)