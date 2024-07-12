n = int(input())
target = 0
num = 1

while True:
    target += num
    if target >= n: break
    num += 1

print(target)