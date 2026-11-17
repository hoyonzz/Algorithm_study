def solution(s):
    answer = 0
    for c in s:
        if c == '(':
            answer += 1
        else:
            answer -= 1
        if answer < 0:
            return False

    if answer == 0:
        return True
    else:
        return False