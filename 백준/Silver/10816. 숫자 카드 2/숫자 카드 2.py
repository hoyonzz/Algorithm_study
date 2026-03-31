import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
keys = list(map(int, input().split()))
m = int(input())
values = list(map(int, input().split()))

keys_counter = Counter(keys)

print(*((keys_counter.get(x, 0) for x in values)))
