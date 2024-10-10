from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([[idx, val] for idx, val in enumerate(priorities)])
    
    while q:
        p = q.popleft()
        if any(p[1] < i[1] for i in q):
            q.append(p)
        else:
            answer += 1
            if p[0] == location:
                return answer