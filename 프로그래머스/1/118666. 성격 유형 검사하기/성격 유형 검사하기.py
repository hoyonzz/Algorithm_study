def solution(survey, choices):
    result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(choices)):
        if choices[i] < 4:
            result[survey[i][0]] += (4-choices[i])
        else:
            result[survey[i][1]] += (choices[i]-4)
    answer = ''
    list_result = list(result.items())
    
    for i in range(4):
        idx = (i*2)
        if list_result[idx][1] >= list_result[idx+1][1]:
            answer += list_result[idx][0]
        else:
            answer += list_result[idx+1][0]
    return answer