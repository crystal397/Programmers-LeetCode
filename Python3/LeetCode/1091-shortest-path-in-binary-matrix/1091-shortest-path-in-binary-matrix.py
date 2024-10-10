from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dr = [1,0,-1,0,1,1,-1,-1]
        dc = [0,1,0,-1,1,-1,-1,1]

        q = deque()
        visited = [[False] * n for _ in range(n)]

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        else:
            start_r, start_c, dist = (0, 0, 1)
            q.append((start_r, start_c, dist))
            visited[start_r][start_c] = True

            while q:
                cur_r, cur_c, dist = q.popleft()

                if cur_r == n-1 and cur_c == n-1:
                    return dist

                for i in range(len(dr)):
                    next_r = cur_r + dr[i]
                    next_c = cur_c + dc[i]

                    if 0 <= next_r < n and 0 <= next_c < n and grid[next_r][next_c] == 0:
                        if visited[next_r][next_c] == False:
                            q.append((next_r, next_c, dist+1))
                            visited[next_r][next_c] = True
            
            return -1