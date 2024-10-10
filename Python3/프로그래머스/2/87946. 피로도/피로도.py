from itertools import permutations

def solution(k, dungeons):
    answer = 0
    answers = []
    kk = k
    per = permutations([i for i in range(len(dungeons))], len(dungeons))
    per = [p for p in per] 
    for i in range(len(per)):
        for j in per[i]:
            if dungeons[j][0] <= kk:
                kk -= dungeons[j][1]
                answer += 1
            else:
                break
        answers.append(answer)
        answer = 0
        kk = k
    return max(answers)