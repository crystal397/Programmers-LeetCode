def solution(citations):
    l = len(citations)
    for i in range(l, 0, -1):
        if len(list(filter(lambda x : x >= i, citations))) >= i:
            return i
    return 0