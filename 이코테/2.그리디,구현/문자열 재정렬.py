S = input()
nums = 0
result = []

for s in S:
    if s.isdigit(): nums += int(s)
    else: result.append(s)

result.sort()
result.append(str(nums))

print(''.join(result))