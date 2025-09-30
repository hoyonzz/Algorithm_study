def solution(n, lost, reserve):
    answer = [0] * n
    for i in lost:
        answer[i-1] -= 1
    for i in reserve:
        answer[i-1] += 1
    
    for i in range(n):
        if answer[i] >= 0:
            pass
        else:
            if i == 0:
                if answer[i+1] > 0:
                    answer[i+1] -= 1
                    answer[i] += 1
            elif i == (n-1):
                if answer[i-1] > 0:
                    answer[i-1] -= 1
                    answer[i] +=1
            else:
                if answer[i-1] > 0:
                    answer[i-1] -= 1
                    answer[i] += 1
                elif answer[i+1] > 0:
                    answer[i+1] -= 1
                    answer[i] += 1
    cnt = 0
    for i in answer:
        if i >= 0:
            cnt += 1
                    
    return cnt