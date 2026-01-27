score = list(map(int, input().strip()))
mid = len(score) // 2

left_score = score[:mid]
right_score = score[mid:]

if sum(left_score) == sum(right_score):
    print("LUCKY")
else:
    print("READY")
