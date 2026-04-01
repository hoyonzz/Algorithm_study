from collections import Counter

def solution(participant, completion):
    answer = ''
    participant = Counter(participant)
    completion = Counter(completion)
    result = list(participant - completion)
    return result[0]