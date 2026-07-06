def solution(n, times):
    s = 1
    e = max(times) * n
    
    while s <= e:
        mid = (s+e) // 2
        result = 0
        for t in times:
            result += mid // t
        if result >= n:
            answer = mid
            e = mid - 1
        else:
            s = mid + 1

    return answer