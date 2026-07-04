def solution(name):
    updown_move = 0

    for c in name:
        if c != 'A':
            updown_move += min(ord(c) - ord('A'), ord('Z')-ord(c)+1)
    
    min_move = len(name) -1
    for idx in range(len(name)):
        next_idx = idx+1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        min_move = min(
            min_move,
            idx * 2 + len(name) - next_idx,
            (len(name) - next_idx) * 2 + idx
        )
    
    return updown_move+min_move