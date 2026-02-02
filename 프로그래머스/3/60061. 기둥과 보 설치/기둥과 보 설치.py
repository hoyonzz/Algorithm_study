def check_possible(answer):
    for x, y, a in answer:
        if a == 0:
            # 기둥일 경우
            if ((y == 0) or
                (x-1, y, 1) in answer or
                (x, y, 1) in answer or
                (x, y-1, 0) in answer):
                continue
            return False
        else:
            if ((x, y-1, 0) in answer or
                (x+1, y-1, 0) in answer or
                ((x-1, y, 1) in answer and (x+1, y, 1) in answer)):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = set()
    for x, y, a, b in build_frame:
        item = (x, y, a)
        
        if b == 1:
            answer.add(item)
            if not check_possible(answer):
                answer.remove(item)
        else:
            answer.remove(item)
            if not check_possible(answer):
                answer.add(item)
    
    return sorted(answer)