from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(computers, visited, start_v):
        q = deque()
        
        q.append(start_v)
        visited[start_v] = True
        
        while q:
            cur_v = q.popleft()
            for next_v, num in enumerate(computers[cur_v]):
                if num == 1 and visited[next_v] == False:
                    q.append(next_v)
                    visited[next_v] =True
    
        return visited
    
    for start_v in range(n):
        if visited[start_v] == False:
            bfs(computers, visited, start_v)
            answer += 1
    
    return answer