import sys
from collections import Counter


input = sys.stdin.readline



s = input().upper().strip()
s_counter = Counter(s).most_common()

if len(s_counter) == 1:
    print(s_counter[0][0])

else:
    if s_counter[0][1] == s_counter[1][1]:
        print('?')
    else:
        print(s_counter[0][0])