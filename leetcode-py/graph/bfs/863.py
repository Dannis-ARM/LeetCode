# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MyNode:
    def __init__(self, x, left = None, right = None, parent = None):
        self.val = x
        self.left = left
        self.right = right
        self.parent = parent

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # find target first 
        # construct a tree that has parent ptr
        # starting from target do the bfs
        # or use dfs, with parent dict to record parents 
        queue = deque()
        queue.append(root)

        parents = {}
        while len(queue) != 0:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parents[node.left] = node
            if node.right:
                queue.append(node.right)
                parents[node.right] = node

        visited = {}
        queue = deque()
        queue.append(target)
        depth = 0
        visited[target] = True

        ans = []
        while len(queue) != 0:
            que_len = len(queue)
            for _ in range(que_len):
                node = queue.popleft()

                if depth == k:
                    ans.append(node.val)
                    continue

                if node.left and node.left not in visited:
                    visited[node.left] = True
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    visited[node.right] = True
                    queue.append(node.right)
                if node in parents and parents[node] not in visited:
                    visited[parents[node]] = True
                    queue.append(parents[node])

            depth += 1
        return ans

        
### TODO 317 questions