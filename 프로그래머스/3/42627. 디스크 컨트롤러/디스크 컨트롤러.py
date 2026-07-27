import heapq
def solution(jobs):
    queue = []
    total_duration = 0
    jobs.sort()
    idx = 0
    current_time = jobs[0][0]
    total_jobs = len(jobs)
    completed_jobs = 0
    while completed_jobs < total_jobs:
        while idx < total_jobs and jobs[idx][0] <= current_time:
            heapq.heappush(queue, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if queue:
            duration, request_time = heapq.heappop(queue)
            current_time += duration
            total_duration += current_time - request_time
            completed_jobs += 1
        else:
            current_time = jobs[idx][0]
            
    return total_duration // total_jobs
    return answer