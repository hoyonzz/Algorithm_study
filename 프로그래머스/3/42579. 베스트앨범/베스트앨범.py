from collections import defaultdict
def solution(genres, plays):
    answer = []
    music = defaultdict(list)
    for i in range(len(genres)):
        music[genres[i]].append([i, plays[i]])
    sorted_music=sorted(music.items(), reverse=True, key=lambda x:sum(song[1] for song in x[1]))
    result = []
    
    for genre, song in sorted_music:
        select_song=sorted(song, key=lambda x:(-x[1],x[0]))
        for i in range(len(select_song)):
            if i > 1: continue
            result.append(select_song[i][0])
    
    return result