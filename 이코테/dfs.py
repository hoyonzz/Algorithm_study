# DFS

# 각 노드가 연결된 정보를 표현(2차원 리스트)
# 1번 노드부터 시작하므로 0번 노드는 비워준다.
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드가 방문된 정보 표현
# 0번 노드포함
visited = [False] * 9


def DFS(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)


DFS(graph, 1, visited)
