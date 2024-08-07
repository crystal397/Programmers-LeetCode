from collections import deque

def solution(s):
    answer = True
    q = deque()
    
    for i in s:
        if i == "(":
            q.append(i)
        else:
            if (len(q) == 0) or ("(" not in q):
                return False
            else:
                q.popleft()
                
    if len(q) != 0:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True