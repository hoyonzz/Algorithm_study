n = input()

answer = 0
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for step1, step2 in steps:
    ny, nx = ord(n[0]), int(n[1])
    nx = nx + step2
    ny = ny + step1

    if nx >= 1 and nx <= 8 and ny <= ord("h") and ny >= ord("a"):
        answer += 1

print(answer)
