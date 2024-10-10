def solution(genres, plays):
    answer = []
    
    # 장르별 총 재생횟수 계산
    # 해시 형태로 장르별 재생횟수, 인덱스 넣기
    most_plays = {}
    genres_plays = {}
    for i in range(len(genres)):
        most_plays[genres[i]] = most_plays.get(genres[i],0) + plays[i]
        genres_plays[i] = [genres[i], plays[i]]

    # 재생된 장르가 많은 순서대로 내림차순 정렬
    sorted_most_plays = dict(sorted(most_plays.items(), key=lambda x: x[1], reverse=True))
    sorted_genres_plays = dict(sorted(genres_plays.items(), key=lambda x: x[1][1], reverse=True))
    
    # 
    for g, p in sorted_most_plays.items():
        cnt = 0
        for k, v in sorted_genres_plays.items():
            if v[0] == g and cnt < 2:
                answer.append(k)
                cnt += 1
                
    return answer