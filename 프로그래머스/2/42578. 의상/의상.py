from collections import defaultdict
def solution(clothes):
    clothes_dict = defaultdict(int)
    for cloth, types in clothes:
        clothes_dict[types] += 1
    answer = 1
    for i in clothes_dict.values():
        answer *= (i+1)
    return answer - 1