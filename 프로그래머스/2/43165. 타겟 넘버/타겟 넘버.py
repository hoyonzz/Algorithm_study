def solution(numbers, target):
    answer = 0
    # 백트레킹 함수 정의
    def backtracking(value, idx):
        nonlocal answer
        if idx == len(numbers):
            if value == target:
                answer += 1
            return
        backtracking(value + numbers[idx], idx + 1)
        backtracking(value - numbers[idx], idx + 1)
    backtracking(0, 0)    
    return answer