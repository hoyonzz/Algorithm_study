def solution(n, lost, reserve):
    # 실제 빌려 줄 수 있는 학생
    set_reserve = set(reserve) - set(lost)
    # 체육복이 없는 학생
    set_lost = set(lost)-set(reserve)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    return n - len(set_lost)
