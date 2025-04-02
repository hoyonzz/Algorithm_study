n = int(input())
members = list(map(int, input().split()))

members.sort()

groups = 0
count = 0

for member in members:
    # 현재 그룹에 해당 모험가를 추가
    count += 1
    # 현재 그룹에 포함된 모험가의 수가 현재의 공포 이상이라면 그룹 결성
    if count >= member:
        groups += 1
        count = 0

print(groups)

