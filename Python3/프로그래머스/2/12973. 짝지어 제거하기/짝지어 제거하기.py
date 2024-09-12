from collections import deque

def solution(s):
    if len(s) == 0:
        return 1
    
    stack = deque()
    stack.append(s[0])
    
    for i in range(1, len(s)):
        if len(stack) != 0 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
            
    if len(stack) == 0:
        return 1
    else:    
        return 0

        

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')