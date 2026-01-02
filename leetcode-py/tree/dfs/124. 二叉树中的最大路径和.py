# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # maxPathSum that pass cur node = max(left, 0) + max(right, 0) + cur.val
        # if cur node is None return 0
        if not root:
            return 0

        global_max = -float('inf')
        def max_path_sum(root):
            nonlocal global_max
            if not root:
                return 0
            
            left_max = max(max_path_sum(root.left), 0)
            right_max = max(max_path_sum(root.right), 0)
            left_right_max = max(left_max, right_max) 

            cur_val = root.val + left_right_max
            cur_max = root.val + left_max + right_max
            global_max = max(global_max, cur_max)
            return cur_val
        
        max_path_sum(root)
        return global_max