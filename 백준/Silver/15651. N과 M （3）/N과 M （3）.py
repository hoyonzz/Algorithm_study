import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())

array = [x for x in range(1, n+1)]

for answer in list(product(array, repeat=m)):
    print(*answer)