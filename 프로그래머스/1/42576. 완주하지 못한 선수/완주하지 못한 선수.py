from collections import Counter

def solution(participant, completion):

    counter_p = Counter(participant)
    counter_c = Counter(completion)
    result = counter_p - counter_c

    result_p = [key for key in counter_p.keys() if key in result]

    return result_p[0]

