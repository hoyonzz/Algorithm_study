import re

def solution(new_id):
    answer = ''
    # 1단계_대문자를 소문자로 치환
    new_id = new_id.lower()
    # 2단계_알파벳 소문자, 숫자, -, _, .를 제외한 문제 제거
    for char in new_id:
        if char.isalnum() or char in '-_.':
            answer += char
    # 3단계_마침표 2번 이상 -> 하나로
    answer = re.sub(r"\.{2,}", ".", answer)
    # 4단계_마침표가 처음이나 끝에 있다면 제거
    answer = answer.strip('.')
    # 5단계_빈 문자열이라면, a를 대입
    if answer == '': 
        answer += 'a'
    # 6단계_길이 16자 이상이면, 제거
    answer = answer[:15]
    answer = answer.rstrip('.')
    # 7단계_ 길이가 2자 이하라면, 반복해서 끝에 붙임
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer