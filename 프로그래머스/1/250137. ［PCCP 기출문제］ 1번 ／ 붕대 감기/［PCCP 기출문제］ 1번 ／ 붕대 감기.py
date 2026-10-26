def solution(bandage, health, attacks):
    now_time = 0
    now_health = health
    for attack in attacks:
        if now_health < health:
            # 힐량 계산하기
            heal_time = attack[0] - now_time 
            heal = (bandage[1] * heal_time) + (heal_time // bandage[0] * bandage[2])
            now_health += heal
            if now_health > health:
                now_health = health
        # 공격계산
        now_health -= attack[1]
        now_time = attack[0] + 1
        if now_health <= 0:
            return -1
        

    return now_health