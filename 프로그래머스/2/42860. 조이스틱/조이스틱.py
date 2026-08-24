def solution(name):
    n = len(name)
    updown_move = 0
    for c in name:
        if c == "A":
            continue
        updown_move += min(
            ord(c) - ord("A"),
            ord('Z') - ord(c) + 1
        )
    
    min_move = n-1
    for i in range(n-1):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        min_move = min(
            min_move,
            (i*2) + n- next_i,
            (n-next_i) * 2 + i
        )
    
    return updown_move + min_move