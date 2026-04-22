def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for i in range(len(name)):
        # 상하 조작
        answer += min(
            (ord(name[i]) - ord('A')),
            (ord('Z') - ord(name[i]) + 1)
        )
        
        next_i = i+1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
            
        # 좌우 조작
        min_move = min(
            min_move,
            ((2*i) + len(name) - next_i),
            (2*(len(name)-next_i) + i)
        )
        
    answer += min_move
    return answer