import re
def solution(dartResult):
    p = r'([0-9]+)([SDT])([*#]?)'
    m = re.findall(p, dartResult)
    
    scores = []
    bonus = {'S':1, 'D':2, 'T':3}
    award = {'': 1, '*':2, '#':-1}
    
    for i, (score, b, a) in enumerate(m):
        if i >= 1 and a == '*':
            scores[i-1]*=2
            
        s = int(score) ** bonus[b] * award[a]
        scores.append(s)
    return sum(scores)