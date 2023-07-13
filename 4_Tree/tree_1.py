### 트리 순회 1. 너비우선탐색(BFS)
from collections import deque

def bfs(root):
    visited = []                # visited : 방문 기록
    if root is None:
        return []
    q = deque()                 # q : 방문 예약
    q.append(root)
    while q:
        cur_node = q.popleft()  # cur_node : 현재 노드
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

bfs(root)