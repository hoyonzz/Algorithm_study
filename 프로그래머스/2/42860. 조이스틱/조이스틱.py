def solution(name):
    n = len(name)
    updown_move = 0
    for c in name:
        if c != 'A':
            updown_move += min(ord(c) - ord('A') , ord('Z') - ord(c) + 1)
    leftright_move = n-1
    for i in range(n):
        next_i = i+1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        leftright_move = min(
            leftright_move,
            (i*2) + n-next_i,
            (n-next_i)*2 + i
        )

    return updown_move + leftright_move