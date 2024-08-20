from collections import Counter

def solution(participant, completion):
    answer = ''
    p = Counter(participant)
    c = Counter(completion)
    i = p - c
    for a in i.keys():
        answer = a
    return answer