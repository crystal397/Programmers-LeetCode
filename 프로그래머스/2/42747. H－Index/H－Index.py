def solution(citations):
    l = len(citations)
    if set(citations) == {0}:
        return 0
    for i in range(l, 0, -1):
        if len(list(filter(lambda x : x >= i, citations))) >= i:
            return i