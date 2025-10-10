def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10, 20, 30, 40]
    current_discounts = []
    
    def dfs(depth):
        if depth == len(emoticons):
            sub, sales = 0, 0
            for user_rate, user_price in users:
                purchase_price = 0
                for i in range(len(emoticons)):
                    if user_rate <= current_discounts[i]:
                        purchase_price += emoticons[i] * (100-current_discounts[i]) // 100
                if purchase_price >= user_price:
                            purchase_price = 0
                            sub += 1
                else:
                    sales += purchase_price
                            
            if answer[0] < sub:
                answer[0], answer[1] = sub, sales
            elif answer[0] == sub and answer[1] < sales:
                answer[1] = sales
            return
        
        # 백트레킹
        for rate in discounts:
            current_discounts.append(rate)
            dfs(depth+1)
            current_discounts.pop()
    
    dfs(0)
                        
    return answer