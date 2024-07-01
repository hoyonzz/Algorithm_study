def solution(num_list):
    sum_odd = ''
    sum_even = ''
    for i in num_list:
        if i % 2 == 1:
            sum_odd += str(i)
        else:
            sum_even += str(i)
    return int(sum_odd) + int(sum_even)