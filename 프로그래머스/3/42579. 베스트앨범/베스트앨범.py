from collections import defaultdict
def solution(genres, plays):
    sum_genres = defaultdict(int)
    musics = defaultdict(list)
    answer = []
    for i in range(len(genres)):
        sum_genres[genres[i]] += plays[i]
        musics[genres[i]].append((plays[i], i))
    # 장르별 내림차순 정렬
    sum_genres = sorted(sum_genres.items(), key=lambda x:x[1], reverse=True)
    # 순회하며 정렬, 두곡씩 정답 저장
    for genre, total in sum_genres:    
        music = sorted(musics[genre], key=lambda x: (
            -x[0],
            x[1]
        ))
        for play, i in music[:2]:
            answer.append(i)
    return answer