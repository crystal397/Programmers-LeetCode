def solution(n):
    answer = 0
    mid = []
    
    # initial
    share = n // 3
    remain = n % 3
    mid.append(remain)
    
    # iterate
    while share != 0:
        remain = share % 3
        mid.append(remain)
        share = share // 3
    
    mid.reverse()
    
    for i in range(len(mid)-1,-1,-1):
        answer += mid[i] * 3**i
    
    return answer