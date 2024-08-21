from collections import deque

def solution(maps):
    answer = 0

    q = deque()
    row = len(maps)
    col = len(maps[0])
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    visited = [[False] * col for _ in range(row)]
    
    q.append((0,0,1))
    visited[0][0] = True
    
    while q:
        cr, cc, dst = q.popleft()
        if (cr, cc) == (row-1, col-1):
            return dst
        else:
            for i in range(len(dr)):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0 <= nr < row and 0 <= nc < col and maps[nr][nc] == 1:
                    if visited[nr][nc] == False:
                        q.append((nr, nc, dst+1))
                        visited[nr][nc] = True

    if visited[row-1][col-1] == False:
        return -1
    
    return answer