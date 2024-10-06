from functools import cmp_to_key

def compare(x,y):
    if str(x)+str(y) <= str(y)+str(x):
        return 1
    else:
        return -1

def solution(numbers):
    answer = ''
    numbers=sorted(numbers, key=cmp_to_key(compare))
    answer = str(int("".join(map(str,numbers))))
    return answer