def solution(s):
    result = 0
    for i in range(len(s)):
        if s[i] == '(':
            result += 1
        elif s[i] == ')':
            result -= 1
        if result < 0:
            return False
    if result == 0:
        return True
    else:
        return False