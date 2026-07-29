import heapq
def solution(operations):
    min_h, max_h, visited = [], [], []
    id_count = 0
    for operation in operations:
        o, num = operation.split()
        num = int(num)
        if o == 'I':
            heapq.heappush(min_h, (num, id_count))
            heapq.heappush(max_h, (-num, id_count))
            visited += [True]
            id_count += 1
        else:
            if num == 1:
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[heapq.heappop(max_h)[1]] = False
            else:
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[heapq.heappop(min_h)[1]] = False
                    
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
        
    if not min_h and not max_h:
        return [0,0]
    return [-max_h[0][0],min_h[0][0]]