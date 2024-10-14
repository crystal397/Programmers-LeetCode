import sys

while True:
    input = sys.stdin.readline
    A, B, C = map(int, input().split())

    if A == B == C == 0:
        break
    if (A + B + C - max(A, B, C)) <= max(A, B, C):
        print('Invalid')
    elif A == B == C:
        print('Equilateral')
    elif A == B or A == C or B == C:
        print('Isosceles')
    else:
        print('Scalene')