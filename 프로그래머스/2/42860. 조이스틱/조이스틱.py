def solution(name):
    n = len(name)
    answer = 0
    
    # 조이스틱 상하 이동
    for c in name:
        if c != 'A':
            answer += min(ord(c)-ord('A'), ord('Z') - ord(c) + 1)
        
    # 조이스틱 좌우 이동
    min_move = n-1
    for i in range(n):
        next_idx = i+1
        while next_idx < n and name[next_idx] =='A':
            next_idx += 1
        min_move = min(min_move, (i*2)+(n-next_idx), 2*(n-next_idx) + i)
    print(answer, min_move)
    return answer+min_move