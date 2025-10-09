def backtrack(path, vistied):
    # m개를 모두 선택했을 때
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(1, n+1):
        # 1부터 n까지 숫자 중에서 선택
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtrack(path, visited)
            path.pop()
            visited[i] = False

n, m = map(int, input().split())
visited = [False] * (n+1)
backtrack([], visited)
