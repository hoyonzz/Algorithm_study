from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque()
    visited = [False] * len(words)
    queue.append((begin, 0))
    while queue:
        word, step = queue.popleft()
        if word == target:
            return step
        for i in range(len(words)):
            if not visited[i]:
                count = 0
                for j in range(len(begin)):
                    if word[j] != words[i][j]:
                        count += 1
                if count == 1:
                    visited[i] = True
                    queue.append((words[i], step +1 ))
    return 0