def solution(price, money, count):
    sumA = 0

    for i in range(count):
        sumA += price * (i + 1)
        
    if sumA <= money:
        return 0
    else:
        return sumA - money
