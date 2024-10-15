from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    mapxy = [[-1]*102 for _ in range(102)]
    visited = [[False]*102 for _ in range(102)]
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    q = deque()
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    q.append((cx,cy))
    visited[cx][cy] = True
    
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x:x*2, r)
        
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    mapxy[i][j] = 0
                elif mapxy[i][j] != 0:
                    mapxy[i][j] = 1
    
    while q:
        x, y = q.popleft()        
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<102 and 0<=ny<102:
                if mapxy[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] =True
                    q.append((nx,ny))
                    mapxy[nx][ny] = mapxy[x][y]+1
    
    return mapxy[ix][iy] //2