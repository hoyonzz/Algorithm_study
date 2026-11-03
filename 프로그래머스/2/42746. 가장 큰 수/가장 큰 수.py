def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x*3, reverse = 1)
    return '0' if str_numbers[0] =='0' else ''.join(str_numbers)