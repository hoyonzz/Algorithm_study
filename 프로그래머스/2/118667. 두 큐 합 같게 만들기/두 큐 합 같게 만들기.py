from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    if (sum1+sum2) % 2 == 1:
        return -1
    target = (sum1+sum2) // 2
    while True:
        if sum1 == target:
            return answer
        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            sum1 += num
            sum2 -= num
        answer += 1
        if answer > len(queue1)*4:
            return -1
