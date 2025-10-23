from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)
    for cloth, type in clothes:
        clothes_dict[type] += 1
    for type, count in clothes_dict.items():
        answer *= count+1
    return answer - 1