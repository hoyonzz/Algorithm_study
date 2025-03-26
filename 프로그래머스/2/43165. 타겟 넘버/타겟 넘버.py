from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    # idx, num
    queue.append((0, 0))
    
    while queue:
        idx, num = queue.popleft()
        if idx == len(numbers):
            if num == target:
                answer += 1
        else:
            queue.append((idx + 1,num + numbers[idx]))
            queue.append((idx + 1,num - numbers[idx]))

    return answer