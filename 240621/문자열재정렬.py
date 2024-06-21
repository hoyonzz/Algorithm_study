S = input()
stack = []
sum = 0
temp = []

for s in S:
    if s.isdigit():
        sum += int(s)
    else:
        while stack and ord(stack[-1]) > ord(s):
            temp.append(stack.pop())
        stack.append(s)
        while temp:
            stack.append(temp.pop())


answer = "".join(stack) + str(sum)
print(answer)

S = input()

sum = 0
num_cnt = 0
arr = []

for s in S:
    if s.isdigit():
        num_cnt += 1
        sum += int(s)
    else:
        arr.append(s)

arr.sort()

if num_cnt > 0:
    arr.append(str(sum))

answer = "".join(arr)
print(answer)
