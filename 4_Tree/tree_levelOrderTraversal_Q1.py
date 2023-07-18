from collections import deque

def maxDepth(root):
    max_dept = 0
    if root is None:
        return max_dept
    q = deque()
    q.append((root, 1))
    while q:
        cur_node, cur_dept = q.popleft()
        max_dept = max(max_dept, cur_dept)
        if cur_node.left:
            q.append((cur_node.left, cur_dept + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_dept + 1))
    return max_dept

class TreeNode:
    def __init__(self, l = None, r = None, v = 0):
        self.left = l
        self.right = r
        self.value = v

root = TreeNode(v = 3)
root.left = TreeNode(v = 9)
root.right = TreeNode(v = 20)
root.right.left = TreeNode(v = 15)
root.right.right = TreeNode(v = 7)

maxDepth(root)