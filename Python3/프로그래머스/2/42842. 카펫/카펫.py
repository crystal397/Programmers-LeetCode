def solution(brown, yellow):
    for i in range(1, ((brown + yellow)//2)+1):
        if ((brown + yellow) % i) == 0:
            j = (brown + yellow) / i
            if (brown == j*2 + (i-2)*2) and (yellow == (j-2)*(i-2)):
                return [j, i]