"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # bfs

        if not root:
            return []

        queue = deque()
        queue.append(root)

        ans = []
        while len(queue) != 0:

            level = []

            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    if child:
                        queue.append(child)
            ans.append(level)
        return ans