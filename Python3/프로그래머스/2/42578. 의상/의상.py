from collections import Counter
import math

def solution(clothes):
    answer = 0
    v = Counter([c[1] for c in clothes])
    k = list(v.values())
    answer = math.prod([i+1 for i in k]) - 1
    return answer