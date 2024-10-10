def solution(n,a,b):
    answer = 1
    count = n/2
    
    while count:
        if (a % 2) == 0 and (b % 2) == 0:
            a /= 2
            b /= 2
        elif (a % 2) == 1 and (b % 2) == 1:
            a = (a + 1) / 2
            b = (b + 1) / 2  
        elif (b % 2) == 1:
            if a//2 == (b+1)//2:
                return answer
            else:
                a /= 2
                b = (b + 1) / 2   
        else:
            if (a+1)//2 == b//2:
                return answer
            else:
                a = (a + 1) / 2
                b /= 2             
        count -= 1
        answer += 1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer