def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    for i in range(len(d)):
        answer += d[i]
        if budget < answer:
            return i
        elif budget == answer:
            return i+1
    return len(d)