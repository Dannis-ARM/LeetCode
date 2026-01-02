# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 9        
        
        sum = 0
        pass_val = 0

        def dfs(node):
            if not node:
                return

            nonlocal sum
            nonlocal pass_val
            
            cur_val = pass_val * 10 + node.val

            if node.left is None and node.right is None:
                sum += cur_val

            pass_val = cur_val
            if node.left:
                dfs(node.left)
            pass_val = cur_val
            if node.right:
                dfs(node.right) 
        dfs(root)
        return sum
        