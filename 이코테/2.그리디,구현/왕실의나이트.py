coordinate = input()
x, y = int(coordinate[1]) , ord(coordinate[0])-ord('a')


moves = [
    (2, -1), (2, 1), (-2, -1), (-1, -2), (1, -2), (-1, 2), (1, 2), (-2, 1)
]

count = 0

for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    if 0 < nx < 9 and 0 <= ny <= 7:
        count += 1

print(count)