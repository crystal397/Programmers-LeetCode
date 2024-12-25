from collections import Counter

def solution(participant, completion):

    p = Counter(participant)
    c = Counter(completion)
    i = p - c
    for key in i.keys():
        return key

