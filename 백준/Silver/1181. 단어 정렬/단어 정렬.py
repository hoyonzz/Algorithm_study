n = int(input())
myset = set()
for i in range(n):
    myset.add(input())

arr = list(myset)
arr.sort(key=lambda word:(len(word),word))

for i in range(len(arr)):
    print(arr[i])
