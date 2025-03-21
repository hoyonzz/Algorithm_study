def solution(numbers):
    str_arr = [str(x) for x in numbers]
    str_arr.sort(key=lambda x:x*3 , reverse=1)
    return str(int(''.join(str_arr)))