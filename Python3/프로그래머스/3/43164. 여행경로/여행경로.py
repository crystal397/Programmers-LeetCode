from collections import deque

def solution(tickets):
    q = deque()
    answer = []
    start = "ICN"
    q.append([start, 0, [start], [False] * len(tickets)])
    
    while q:
        stp, cnt, path, used = q.popleft()
        
        if len(tickets) == cnt:
            answer.append(path)
            continue
           
        for i in range(len(tickets)):
            s, d = tickets[i]
            if s == stp and not used[i]:
                new_used = used[:]
                new_used[i] = True
                new_path = path + [d]
                q.append([d, cnt+1, new_path, new_used])
        
    answer.sort()
    return answer[0]