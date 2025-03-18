n = int(input())
count, sum, start_index, end_index = 1,1,1,1

while end_index != n:
    if sum < n:
        end_index += 1
        sum += end_index
    elif sum == n:
        count += 1
        end_index += 1
        sum += end_index
    else:
        sum -= start_index
        start_index += 1

print(count)