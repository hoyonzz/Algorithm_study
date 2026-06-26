def solution(number, k):
    stack = []
    for i in range(len(number)):
        num = number[i]
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    answer = ''.join(stack)
    
    if k > 0:
        answer = answer[:len(answer)-k]
    
    return answer