def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0: 
                stack.pop()
            else:
                return False
    
    if len(stack) != 0: 
        return False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True