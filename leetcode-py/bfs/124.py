# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxVal = -float('inf')

    def dfs(self, node): # the biggest value that contains this node
        if node is None:
            return 0
        
        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0) 

        self.maxVal = max(self.maxVal, node.val + left + right)
        return max(node.val + left, node.val + right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)  
        return self.maxVal