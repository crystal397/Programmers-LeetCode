def solution(participant, completion):
    answer = ''
    info_player = {}
    for i in participant:
        if i in info_player.keys():
            info_player[i] += 1
        else:
            info_player[i] = 1
    for i in completion:
        if i in info_player.keys():
            info_player[i] -= 1
            if info_player[i] == 0:
                del info_player[i]
    answer = list(info_player.keys())
    return answer[0]