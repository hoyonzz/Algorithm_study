def solution(name):
    n = len(name)
    updown_move = 0
    for c in name:
        updown_move += min(ord(c)-ord('A'), ord('Z')-ord(c)+1)

    min_move = n-1
    for i in range(n):
        next_idx = i+1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        min_move = min(min_move, (i*2) + (n-next_idx), 2*(n-next_idx) + i)
        
        
    return updown_move+min_move