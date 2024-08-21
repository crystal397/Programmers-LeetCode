def solution(prices):
    answer = [0] * len(prices)
    s = []
    
    for i, price in enumerate(prices):
        while s and prices[s[-1]] > price:
            idx = s.pop()
            answer[idx] = i - idx
        s.append(i)
        
    while s:
        idx = s.pop()
        answer[idx] = len(prices) - 1 -idx
    
    return answer