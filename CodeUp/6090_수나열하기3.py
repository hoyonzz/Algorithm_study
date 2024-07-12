a, m, d, n = map(int, input().split())
answer = a

for i in range(n-1):
    answer = answer * m + d
    
print(answer)