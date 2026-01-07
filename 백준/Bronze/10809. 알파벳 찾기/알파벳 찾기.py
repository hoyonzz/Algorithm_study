alpha = [chr(a) for a in range(ord('a'), ord('z')+1)]
s = input()
for a in alpha:
    print(s.find(a), end=' ')