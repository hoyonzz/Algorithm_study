data = input()

result = int(data[0])
# 만약 0 이라면 어떻게 할까?

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 1보다 같거나 작은 경우 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
