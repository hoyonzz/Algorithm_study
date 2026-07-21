def solution(begin, target, words):
    if target not in words:
        return 0
    
    def check_word(word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count == 1:
            return True
        return False
    
    from collections import deque
    queue = deque([(begin, 0)])
    visited = set([begin])
    while queue:
        current_word, current_step = queue.popleft()
        if current_word == target:
            return current_step
        for word in words:
            if word not in visited:
                if check_word(current_word, word):
                    queue.append((word, current_step+1))
                    visited.add(word)
    
    return 0