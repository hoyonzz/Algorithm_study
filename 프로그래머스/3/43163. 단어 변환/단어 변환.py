from collections import deque
# 알파벳 하나만 다른지 판별하는 함수
def is_one_diff(word1, word2):
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
        if diff_count > 1: return 0
    return diff_count == 1

def solution(begin, target, words):
    # 예외처리-target이 words안에 없다면 0 반환
    if target not in words: return 0
    
    # bfs 탐색 준비
    queue = deque()
    queue.append((begin,0))
    visited = {begin}
    
    # bfs 탐색 시작
    while queue:
        word, steps = queue.popleft()
        # 정답이면 단계 반환
        if word == target: return steps
        for next_word in words:
            # 조건1.알파벳검사, 조건2.방문X
            if is_one_diff(word, next_word) and next_word not in visited:
                visited.add(next_word)
                queue.append((next_word, steps+1))
    return 0