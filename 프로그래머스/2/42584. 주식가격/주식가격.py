def solution(prices):
    stack = []
    # 정답리스트 초기화
    answer = [0] * len(prices)
    # # stack에 idx넣으며, 가격이 떨어졌나 체크
    for idx, price in enumerate(prices):
        # 스택이 비어있지 않고, 현재가격이 더 클 때 떨어진 것
        while stack and prices[stack[-1]] > price:
            i = stack.pop()
            answer[i] = idx-i
        stack.append(idx)
    # 현재 스택에는 모두다 떨어지지 않은 값만 남아있음
    while stack:
        i = stack.pop()
        answer[i] = len(prices) - i - 1
    return answer