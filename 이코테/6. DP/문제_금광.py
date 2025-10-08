for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    # dp테이블에 array추가
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    # dp
    for y in range(1, m):
        for x in range(n):
            # case1. 왼쪽 위에서 오는 경우(맨윗칸이라면 제외)
            if x == 0:
                left_up = 0
            else:
                left_up = dp[x-1][y-1]

            # case2. 왼쪽 아래에서 오는 경우(맨 아래칸이라면 제외)
            if x == (n-1):
                left_down = 0
            else:
                left_down = dp[x+1][y-1]

            # case3. 왼쪽에서 오는 경우
            left = dp[x][y-1]

            dp[x][y] = dp[x][y] + max(left_up, left_down, left)

    # 정답 산출
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)