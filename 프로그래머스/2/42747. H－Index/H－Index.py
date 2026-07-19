def solution(citations):
    h = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i+1 <= citations[i]:
            h = i+1
        else:
            break
            
    return h