from collections import deque

def solution(n, computers):
    answer = 0
    a_list = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                a_list[i].append(j)
    
    def bfs(a_list, start_v):
        # initial settings
        q = deque()
        visited = [False] * len(a_list)
    
        # first
        q.append(start_v)
        visited[start_v] = True

        # loop
        while q:
            cur_v = q.popleft()
            for next_v in a_list[cur_v]:
                if visited[next_v] == False:
                    q.append(next_v)
                    visited[next_v] = True
                    
        answer += 1
        
        return answer
    
    for start_v in range(n):
        bfs(a_list, start_v)
            
    return answer