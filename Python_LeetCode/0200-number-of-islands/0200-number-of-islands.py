from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        row = len(grid)
        col = len(grid[0])
        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]

        visited = [[False] * col for _ in range(row)]

        def bfs(r,c):
            q = deque()

            q.append((r,c))
            visited[r][c] = True

            while q:
                cur_r, cur_c = q.popleft()
                for i in range(len(dr)):
                    next_r = cur_r + dr[i]
                    next_c = cur_c + dc[i]

                    if 0 <= next_r < row and 0 <= next_c < col and grid[next_r][next_c] == '1':
                        if visited[next_r][next_c] == False:
                            q.append((next_r, next_c))
                            visited[next_r][next_c] = True

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and visited[r][c] == False:
                    bfs(r,c)
                    answer += 1

        return answer