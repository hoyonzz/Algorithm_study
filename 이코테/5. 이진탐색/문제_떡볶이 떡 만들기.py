# 떡의 개수와 요천한 떡의 길이 입력
n, m = map(int, input().split())

# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += (x - mid)
        
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 탐색)