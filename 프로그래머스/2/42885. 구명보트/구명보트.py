def solution(people, limit):
    # 정렬
    people.sort()
    answer = 0
    # 투포인터 설정
    left, right = 0, len(people) - 1
    # 투포인터 연산
    while left <= right:
        if left == right:
            answer += 1
            break
        weight = people[left] + people[right]
        if limit >= weight:
            answer += 1
            left, right = left + 1, right - 1
        else:
            answer += 1
            right = right - 1
    return answer