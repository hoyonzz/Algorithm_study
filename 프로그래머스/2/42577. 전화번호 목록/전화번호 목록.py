def solution(phone_book):
    answer = True
    hash = dict()
    for phone_number in phone_book:
        hash[phone_number] = True
    
    for numbers in hash:   
        temp = ''
        for i in range(len(numbers)):
            temp += numbers[i]
            if temp in hash and temp != numbers:
                answer = False
                return False
    return answer