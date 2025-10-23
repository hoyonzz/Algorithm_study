from collections import Counter
def solution(clothes):
    counter = Counter([item[1] for item in clothes])
    answer = 1
    for count in counter.values():
        answer *= count + 1
    return answer - 1