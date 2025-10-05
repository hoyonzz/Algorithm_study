import re

def solution(new_id):
    # 1. 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2. 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    
    # 3. 마침표 2번이상 연속된 부분 하나의 마침표로 치환
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    # 4. 처음이나 끝에 . 있다면 제거
    new_id = re.sub(r'^\.|\.$', '', new_id)
    
    # 5. 빈문자열이면 a대입
    if not new_id:
        new_id = 'a'
    
    # 6. 16자 이상이라면 15개만 남기고 마지막이 . 라면제거
    new_id = new_id[:15].rstrip('.')
    
    # 7. 2자 이하라면 마지막 문자가 3글자가 될때까지 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id