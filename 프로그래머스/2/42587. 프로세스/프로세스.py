from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    for idx, priority in enumerate(priorities):
        queue.append((idx, priority))
    while queue:
        i, p = queue.popleft()
        if any(p < x for idx, x in queue):
            queue.append((i, p))
        else:
            answer += 1
            if i == location:
                return answer
            
    
    return answer