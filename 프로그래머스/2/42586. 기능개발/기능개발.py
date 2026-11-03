import math
def solution(progresses, speeds):
    jobs = []
    for i in range(len(progresses)):
        jobs.append(math.ceil((100-progresses[i])/speeds[i]))
    s = jobs[0]
    count = 1
    answer = []
    for j in jobs[1:]:
        if s >= j:
            count+= 1
        else:
            answer.append(count)
            count = 1
            s = j
    answer.append(count)
    return answer