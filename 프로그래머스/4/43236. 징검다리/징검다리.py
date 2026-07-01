def solution(distance, rocks, n):
    rocks.sort()
    start, end = 0, distance
    
    while start <= end:
        mid = (start+end) // 2
        removed_count = 0
        point = 0
        
        for rock in rocks:
            if rock-point >= mid:
                point = rock
            else:
                removed_count += 1
        
        if distance - point < mid:
            removed_count += 1
        
        if removed_count <= n:
            answer = mid
            start = mid + 1
            
        else:
            end = mid - 1
            
    return answer