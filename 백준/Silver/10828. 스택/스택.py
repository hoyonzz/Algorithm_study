import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    com = input().split()
    op = com[0]
    
    if op == 'push':
        stack.append(int(com[1]))
    elif op == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif op == 'size':
        print(len(stack))
    elif op == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])