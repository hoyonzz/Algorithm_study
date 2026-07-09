def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # 숫자 이어붙이기
        dp[i].add(int(str(N) * i))
        
        # 이전 숫자 4칙연산
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    # 더하기
                    dp[i].add(num1+num2)
                    # 빼기
                    dp[i].add(num1-num2)
                    # 나누기 (zero오류 방지)
                    if num2 == 0:
                        continue
                    else:
                        dp[i].add(num1//num2)
                    # 곱하기
                    dp[i].add(num1 * num2)
            if number in dp[i]:
                return i
    return -1