def solution(numbers, target):
    def dfs(value, idx):
        nonlocal answer
        if idx == len(numbers):
            if value == target:
                answer += 1
            return
        dfs(value + numbers[idx], idx + 1)
        dfs(value - numbers[idx], idx + 1)
    answer = 0
    dfs(0, 0)
    return answer