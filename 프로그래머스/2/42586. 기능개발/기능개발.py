from collections import deque
def solution(progresses, speeds):
    q = deque([p, s] for p, s in zip(progresses, speeds))
    answer = []
    while q:
        for job in q:
            job[0] += job[1]
        count = 0
        while q and q[0][0] >= 100:
            q.popleft()
            count += 1
        if count >= 1:
            answer.append(count)
            
    return answer