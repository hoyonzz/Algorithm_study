n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0 
total = 0
start = 0
end = max(arr)

while start <= end:
    mid = (start+end)//2
    total = 0
    # 남은 떡 길이 계산
    for x in arr:
        if x > mid:
            total += x - mid
    
    # 떡의 길이가 m보다 크다면, mid 으론쪽 탐색, 결과값 저장
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)