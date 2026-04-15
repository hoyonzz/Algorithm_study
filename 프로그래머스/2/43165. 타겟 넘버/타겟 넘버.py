def solution(numbers, target):
    answer = 0
    # 백트레킹 함수 구현
    def backtracking(idx, total):
        nonlocal answer
        # 종료조건: idx가 numbers 개수 일 때,
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        backtracking(idx + 1, total+numbers[idx])
        backtracking(idx + 1, total-numbers[idx])
    backtracking(0, 0)

    return answer