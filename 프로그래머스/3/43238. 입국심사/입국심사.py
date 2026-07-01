def solution(n, times):
    start = 0
    end = max(times) * n
    
    while start <= end:
        result = 0
        mid = (start+end) // 2
        
        for i in times:
            result += (mid // i)
        
        if result >= n:
            answer = mid
            end = mid -1
        else:
            start = mid + 1
    
    return answer