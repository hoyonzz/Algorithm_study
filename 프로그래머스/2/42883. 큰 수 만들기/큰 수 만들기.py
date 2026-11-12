def solution(number, k):
    stack = []
    for i in number:
        num = int(i)
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k-=1
        stack.append(num)
    answer = ""
    for i in range(len(stack)-k):
        answer += str(stack[i])
    return answer