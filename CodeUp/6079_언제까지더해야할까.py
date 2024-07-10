n = int(input())
num = 1
total = 1

while True:
    if total >= n:
        break
    num += 1
    total += num

print(num)