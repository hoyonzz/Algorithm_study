def solution(name):
    n = len(name)
    up_down_move = 0
    # 상하이동거리계산
    for c in name:
        up_down_move += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        
    # 좌우 이동거리계산
    min_move = n-1
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        min_move = min(min_move, 2*i+n-next_idx,2*(n-next_idx)+i)

    return min_move + up_down_move