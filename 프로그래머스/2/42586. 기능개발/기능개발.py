from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([p, s] for p, s in zip(progresses, speeds))
    while queue:
        for job in queue:
            job[0] += job[1]
        count = 0
        while queue and queue[0][0] >= 100:
            queue.popleft()
            count += 1
        if count > 0:
            answer.append(count)
    return answer