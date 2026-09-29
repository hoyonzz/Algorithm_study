def solution(name):
    updown_move = 0
    for c in name:
        updown_move += min(
            ord(c) - ord('A'),
            ord('Z') - ord(c) + 1
        )
    min_move = len(name) - 1
    for i in range(len(name)):
        next_idx = i+1
        while next_idx < len(name) and name[next_idx] =='A':
            next_idx += 1
        min_move = min(
            min_move,
            (i*2) + len(name) - next_idx,
            (2*(len(name)-next_idx)) + i
        )
    return min_move + updown_move