# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_d = float("inf")

        queue = [root]
        cur_d = 1
        while len(queue) != 0:
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.pop(0)

                if not node.left and not node.right:
                    min_d = min(min_d, cur_d) 

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            cur_d += 1
        return min_d