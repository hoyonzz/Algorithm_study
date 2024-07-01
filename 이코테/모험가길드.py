n = int(input())
players = list(map(int, input().split()))
members = 0
answer = 0
players.sort()

for i in range(n):
    members += 1
    if members >= players[i]:
        answer += 1
        members = 0

print(answer)
