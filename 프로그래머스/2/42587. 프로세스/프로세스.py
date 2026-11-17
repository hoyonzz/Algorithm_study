from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque((i, p) for i, p in enumerate(priorities))
    while queue:
        q = queue.popleft()
        if any(q[1] < p[1] for p in queue):
            queue.append(q)
        else:
            answer += 1
            if q[0] == location:
                return answer
    
