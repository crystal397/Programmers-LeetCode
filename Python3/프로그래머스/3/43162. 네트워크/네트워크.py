from collections import deque

def bfs(s, computers, visited):
    q = deque()
    
    q.append(s)
    visited[s] = True
    
    while q:
        c = q.popleft()
        for n, cn in enumerate(computers[c]):
            if visited[n] == False and cn == 1:
                q.append(n)
                visited[n] = True
    
    return visited

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
    
    return answer