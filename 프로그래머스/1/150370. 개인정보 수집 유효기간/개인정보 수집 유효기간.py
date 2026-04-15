from collections import defaultdict

def cal_days(num):
    y, m, d = map(int, num.split('.'))
    total = (y*12*28) + (m*28) + d
    return total

def solution(today, terms, privacies):
    answer = []
    dict_terms = defaultdict(int)
    for term in terms:
        t, m = term.split(' ')
        dict_terms[t] = int(m) * 28
    for idx, privacie in enumerate(privacies):
        days, term = privacie.split(' ')
        if cal_days(today) >= cal_days(days) + dict_terms[term]:
            answer.append(idx+1)
        
    return answer

