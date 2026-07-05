def solution(name):
    n = len(name)
    updown_move = 0
    for c in name:
        updown_move += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        
    min_move = n-1
    for idx in range(n):
        next_idx = idx + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        min_move = min(
            min_move,
            idx*2 + n - next_idx,
            (n-next_idx) * 2 + idx
        )

    return updown_move + min_move