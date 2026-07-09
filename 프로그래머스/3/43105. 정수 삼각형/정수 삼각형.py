def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            left_up = triangle[i-1][j-1] if j > 0 else 0
            right_up = triangle[i-1][j] if j < len(triangle[i])-1 else 0
            triangle[i][j] += max(left_up, right_up)
    return max(triangle[len(triangle)-1])