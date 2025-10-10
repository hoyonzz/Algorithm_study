def check(num):
    if len(num) == 1:
        return True
    mid = len(num) // 2
    parent = num[mid]
    left_side = num[:mid]
    right_side = num[mid+1:]

    if parent == '0':
        if '1' in left_side or '1' in right_side:
            return False

    return check(left_side) and check(right_side)

def is_valid_num(num):
    bin_num = format(num, 'b')
    s = len(bin_num)
    i, n = 0, 0
    while n < s:
        n = 2 ** i - 1
        i += 1

    binary_num = ('0'*(n-s)) + bin_num

    return check(binary_num)

def solution(numbers):
    answer = []
    

    
    for number in numbers:
        if is_valid_num(number):
            answer.append(1)
        else:
            answer.append(0)
    return answer