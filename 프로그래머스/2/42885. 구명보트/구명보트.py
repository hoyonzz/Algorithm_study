def solution(people, limit):
    s, e = 0, len(people)-1
    people.sort()
    answer = 0
    while s <= e:
        if people[s] + people[e] > limit:
            e -= 1
        else:
            s += 1
            e -= 1
        answer += 1
        
    return answer