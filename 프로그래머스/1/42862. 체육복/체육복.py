def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    answer = n - len(set_lost)
    
    for i in range(1, n+1):
        if i in set_reserve:
            if i-1 in set_lost:
                set_lost.remove(i-1)
                answer += 1
            elif i+1 in set_lost:
                set_lost.remove(i+1)
                answer += 1
    return answer