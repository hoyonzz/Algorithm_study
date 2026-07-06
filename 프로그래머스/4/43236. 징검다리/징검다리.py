def solution(distance, rocks, n):
    rocks.sort()
    s = 1
    e = distance

    while s <= e:
        mid = (s + e) // 2
        count = 0
        point = 0
        for rock in rocks:
            if rock-point < mid:
                count += 1
            else:
                point = rock
        
        if distance-point < mid:
            count += 1
        
        if count <= n:
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
            
    return answer