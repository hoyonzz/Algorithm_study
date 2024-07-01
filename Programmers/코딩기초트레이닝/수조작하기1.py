def solution(n, control):
    answer = n
    for s in control:
        if s == 'w':
            answer += 1
        elif s == 's':
            answer -= 1
        elif s == 'd':
            answer += 10
        elif s == 'a':
            answer -= 10
            
    return answer