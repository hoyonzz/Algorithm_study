def solution(cap, n, deliveries, pickups):
    d_rem, p_rem = 0, 0
    answer = 0
    for i in range(n-1, -1, -1):
        d_rem += deliveries[i]
        p_rem += pickups[i]
        while d_rem > 0 or p_rem > 0:
            answer += (i+1) * 2
            d_rem -= cap
            p_rem -= cap
    
    return answer