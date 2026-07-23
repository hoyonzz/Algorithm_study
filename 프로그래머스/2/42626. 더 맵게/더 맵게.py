def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while scoville and len(scoville) > 1:
        s1 = heapq.heappop(scoville)
        if s1 >= K:
            break
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1+(s2*2))
        answer += 1
    if scoville[-1] < K:
        return -1
    return answer
    
            