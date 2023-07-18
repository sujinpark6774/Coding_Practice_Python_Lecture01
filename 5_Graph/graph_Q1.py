### Q1. Number Of Islands
### https://www.notion.so/1-Graph-8764195ab82a445e8ec42cc0208ba60d

### 1. BFS 풀이
from collections import deque

def numIslands(grid):
    number_of_islands = 0
    m = len(grid)
    n = len(grid[0])
    visited = [[False] * n for _ in range(m)]

    def bfs(x, y):
        # 상, 하, 좌, 우 <- 4가지 경우로 움직이기 위해 생성. 만약, 대각선 방향도 추가하고 싶으면 해당 방향에 맞게 dx, dy 추가하면 됨
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        visited[x][y] = True
        queue = deque()
        queue.append((x, y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):   # 상, 하, 좌, 우 <- 4가지 경우이기 때문에 4로 설정. But, 대각선 방향도 추가한다면 추가되는 방향만큼 횟수 up
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]

                # 방문하면 안 되는 곳을 제외하고 방문해야 함
                # 1. 인덱스 값이 grid의 범위를 넘어가는 경우는 제외
                # 2. 이미 방문한 경우는 제외
                # 3. 값이 0인 경우는 제외
                if (next_x >= 0 and next_x < m and next_y >= 0 and next_y < n):
                    if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                bfs(i, j)
                number_of_islands += 1
    return number_of_islands



numIslands(grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['1', '1', '0', '1', '1'],
])