# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # find right node for each level
        if not root:
            return []

        ans = []
        queue = [root]
        while len(queue) != 0:
            length = len(queue)
            ans.append(queue[-1].val)
            for _ in range(length):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans