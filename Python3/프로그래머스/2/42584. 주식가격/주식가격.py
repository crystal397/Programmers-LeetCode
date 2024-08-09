def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for idx, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            pop_idx = stack.pop()
            answer[pop_idx] = idx - pop_idx
        stack.append(idx)
    
    while len(stack) != 0:
        pop_idx = stack.pop()
        answer[pop_idx] = len(prices) - 1 - pop_idx
    
    return answer