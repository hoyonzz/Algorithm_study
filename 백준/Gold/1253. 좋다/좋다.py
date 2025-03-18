n = int(input())
arr = list(map(int, input().split()))
count = 0


arr.sort()

for k in range(n):
    i, j = 0, (n-1)
    while i < j:
        if arr[i]+arr[j] < arr[k]:
            i += 1
        elif arr[i]+arr[j] > arr[k]:
            j -= 1
        else:
            if i != k and j != k:
                count += 1
                break
            elif j == k:
                j -= 1
            else:
                i += 1 

print(count)