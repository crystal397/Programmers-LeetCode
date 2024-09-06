from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque()
    l = len(progresses)
    
    for i in range(l):
        p = 100 - progresses[i]
        q.append(math.ceil(p / speeds[i]))
    
    while q:
        cur = q.popleft()
        count = 1
        while q and q[0] <= cur:
            q.popleft()
            count += 1
        answer.append(count)
    return answer