def solution(name):
    updown_move = 0
    for i, char in enumerate(name):
        if char != 'A':
            updown_move += min((ord(char)-ord('A')), (ord('Z')-ord(char)+1))
    
    min_move = len(name)-1

    for i, char in enumerate(name):
        next_idx = i+1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        
        move_a = i*2 + len(name)-next_idx
        move_b = (len(name)-next_idx)*2 + i
        min_move = min(min_move, move_a, move_b)
    
    return updown_move + min_move
                               
    