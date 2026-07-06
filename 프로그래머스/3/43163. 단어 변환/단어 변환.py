def solution(begin, target, words):
    if target not in words:
        return 0
    
    def check_word(a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
            if count > 1:
                break
        if count == 1:
            return True
        return False
    
    def bfs(word, count):
        from collections import deque
        queue = deque()
        queue.append((word, count))
        while queue:
            a, count = queue.popleft()
            if a == target:
                return count
            for b in words:
                if check_word(a, b):
                    queue.append((b, count + 1))


    
    return bfs(begin, 0)