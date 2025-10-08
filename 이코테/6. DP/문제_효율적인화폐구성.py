n , m = map(int, input().split())
money = [] 
for _ in range(n):
    money.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for coin in money:
    for i in range(coin, m+1):
        if d[i-coin] != 10001:
            d[i] = min(d[i], d[i-coin] + 1)

if d[m] != 10001:
    print(d[m])
else:
    print(-1)