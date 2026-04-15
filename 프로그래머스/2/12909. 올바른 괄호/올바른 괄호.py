def solution(s):
    if len(s) % 2 != 0 or s[0] == ')':
        return False
    
    count = 0
    
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False