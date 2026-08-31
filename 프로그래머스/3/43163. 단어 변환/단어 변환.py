from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = set([begin])
    
    def bfs(word, cnt):
        queue = deque()
        queue.append((word, cnt))
        while queue:
            w, step = queue.popleft()
            if w == target:
                return step
            
            for next_word in words:
                if next_word not in visited and sum(c1 != c2 for c1, c2 in zip(w, next_word)) == 1:
                    visited.add(next_word)
                    queue.append((next_word, step+1))
        return 0
    
    return bfs(begin, 0)