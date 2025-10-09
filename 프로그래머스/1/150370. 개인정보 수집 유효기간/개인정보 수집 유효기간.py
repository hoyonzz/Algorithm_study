def solution(today, terms, privacies):
    answer = []
    terms_dic = {}
    for i in range(len(terms)):
        key, value = terms[i].split()
        terms_dic[key] = int(value)
    
    today_year, today_month, today_day = map(int, today.split('.'))
    today_days = (((today_year * 12) + today_month) * 28) + today_day
    
    for idx, privacy in enumerate(privacies):
        privacy_date, privacy_term = privacy.split()
        privacy_year, privacy_month, privacy_day = map(int, privacy_date.split('.'))
        privacy_days = ((privacy_year * 12) + privacy_month + terms_dic[privacy_term])* 28 + privacy_day
        # 오늘 날짜가 유효기간이 지났다면,
        if today_days >= privacy_days:
            answer.append(idx + 1)
    return answer