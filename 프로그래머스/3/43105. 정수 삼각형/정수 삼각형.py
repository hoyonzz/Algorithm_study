def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            up = triangle[i-1][j] if j < len(triangle[i]) - 1 else 0
            up_left = triangle[i-1][j-1] if j > 0 else 0

            triangle[i][j] += max(up_left, up)
            
            
    return max(triangle[len(triangle)-1])