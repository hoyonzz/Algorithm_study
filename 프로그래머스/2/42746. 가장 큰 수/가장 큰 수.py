def solution(numbers):
    arr = [str(x) for x in numbers]
    arr.sort(reverse=True, key=lambda x: x*3)
    if arr[0] == '0':
        return '0'
    answer = ''.join(arr)
    return answer