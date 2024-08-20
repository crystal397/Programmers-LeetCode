from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    
    q = deque()
    visited = [[False] * col for _ in range(row)]
    
    sr, sc, dst = (0,0,1)
    q.append((sr, sc, dst))
    visited[sr][sc] == True
    
    while q:
        cr, cc, dst = q.popleft()
        if cr == row -1 and cc == col -1:
            return dst

        for i in range(len(dr)):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < row and 0 <= nc < col and maps[nr][nc] == 1:
                if visited[nr][nc] == False:
                    q.append((nr,nc,dst+1))
                    visited[nr][nc] = True
    
    return -1