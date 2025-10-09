from itertools import combinations
heights = []

for _ in range(9):
    heights.append(int(input()))

for comb in combinations(heights, 7):
    if sum(comb) == 100:
        result = sorted(comb)

for i in result:
    print(i)