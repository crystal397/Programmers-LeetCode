from collections import Counter

def solution(participant, completion):    
    counter_p = Counter(participant)
    counter_c = Counter(completion)
    
    common_diff = counter_p - counter_c
    
    for key in common_diff.keys():
        return key