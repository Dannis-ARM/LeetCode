# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, curD, maxDList):
        if root is None:
            return 
        
        maxDList[0] = max(maxDList[0], curD)

        self.dfs(root.left, curD+1, maxDList)
        self.dfs(root.right, curD+1, maxDList)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = list()
        res.append(1)

        self.dfs(root, 1, res)

        return res[0]


"""
use a nicer way to solve this 
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        

"""
use bfs
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # bfs to get depth
        que = list()
        que.append(root)
        d = 0

        while (len(que) != 0):
            for _ in range(len(que)):
                node = que.pop(0)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            d += 1
        return d
