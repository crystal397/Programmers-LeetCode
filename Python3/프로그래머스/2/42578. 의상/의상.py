from collections import Counter
import math

def solution(clothes):
    answer = 0
    v = Counter([c[1] for c in clothes]) # 같은 종류의 카테고리끼리 묶기 + 묶은 카테고리의 종류는 각각 몇 개인지 파악
    k = list(v.values())
    answer = math.prod([i+1 for i in k]) - 1 # 리스트 내 모든 값 곱하기
    return answer
