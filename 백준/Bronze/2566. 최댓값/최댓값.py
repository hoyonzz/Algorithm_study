max_value, max_row, max_col = -1, -1, -1

for i in range(1, 10):
    row = list(map(int, input().split()))
    tmp = max(row)
    if max_value < tmp:
        max_row = i
        max_col = row.index(tmp) + 1
        max_value = tmp

print(max_value)
print(max_row, max_col)