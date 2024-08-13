class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def bfs(rooms, start_v=0):
            # initial settings
            q = deque()
            visited = [False] * len(rooms)
            # first
            q.append(start_v)
            visited[start_v] = True
            # using loop
            while q:
                cur_v = q.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        q.append(next_v)
                        visited[next_v] = True
            return all(visited)

        # find
        return bfs(rooms, start_v=0)