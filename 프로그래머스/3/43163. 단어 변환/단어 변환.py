def solution(begin, target, words):
    def check_words(a, b):
        check = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                check += 1
        if check == 1:
            return True
        return False
    
    visited = [False] * len(words)
    answer = 0
    
    from collections import deque
    def bfs(start, count):
        queue = deque()
        queue.append((start, 0))
        while queue:
            word, count = queue.popleft()
            if word == target:
                return count
            for i in range(len(words)):
                if not visited[i] and check_words(word, words[i]):
                    queue.append((words[i], count + 1))
                    visited[i] = True
    answer = bfs(begin, 0)
    if target not in words:
        return 0
    return answer