def solution(citations):
    citations.sort(reverse=True)
    count = 0
    for i in range(len(citations)):
        if count >= citations[i]:
            break
        count += 1
    return count