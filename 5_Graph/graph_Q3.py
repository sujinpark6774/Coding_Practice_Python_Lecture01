### Q3. Keys and Rooms
### https://www.notion.so/1-Graph-8764195ab82a445e8ec42cc0208ba60d

### DFS 풀이
def canVisitAllRoomsDFS(rooms):
    visited = [False] * len(rooms)

    # v에 연결되어 있는 모든 vertex에 방문할 것이다.    
    def dfs(v):
        visited[v] = True
        for next_v in rooms[v]:
            if visited[next_v] == False:
                dfs(next_v)

    dfs(0)

    if len(visited) == len(rooms):
        return True
    else:
        return False
    
from collections import deque
### BFS 풀이
def canVisitAllRoomsBFS(rooms):
    visited = [False] * len(rooms)

    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if visited[next_v] == False:
                    queue.append(next_v)
                    visited[next_v] = True

    bfs(0)

    return all(visited)



rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]

canVisitAllRoomsDFS(rooms)
canVisitAllRoomsBFS(rooms)