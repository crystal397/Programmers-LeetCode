from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for start_v in range(n):
        if visited[start_v] == False:
            bfs(computers, start_v, visited)
            answer += 1
                
    return answer

def bfs(computers, start_v, visited):
    q = deque()
    
    q.append(start_v)
    visited[start_v] = True
    
    while q:
        cur_v = q.popleft()
        for next_v, num in enumerate(computers[cur_v]):
            if visited[next_v] == False and num == 1:
                q.append(next_v)
                visited[next_v] = True
    return visited