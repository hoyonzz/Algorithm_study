def solution(phone_book):
    answer = True
    hash_map = {}
    for phone in phone_book:
        hash_map[phone] = 0
    for phone in phone_book:
        mixture = []
        temp = ''
        for i in range(len(phone)-1):
            temp += phone[i]
            mixture.append(temp)
        for num in mixture:
            if num in hash_map.keys():
                return False
    return answer