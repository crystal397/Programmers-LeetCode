from itertools import permutations

def solution(numbers):
    answer = 0
    number = []
    for i in range(1, len(numbers)+1):
        number.extend(''.join(c) for c in permutations(numbers, i))
        number = list(set(map(int, number)))
    for i in number:
        if is_Prime(i):
            print(i)
            answer += 1
    return answer

def is_Prime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True