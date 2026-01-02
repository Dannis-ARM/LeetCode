# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # is_avl()
        # def get_depth()
        # abs(left_d - right_d) <= 1 and is_avl(node.left) and is_avl_node.right

        def get_depth(node):
            if not node:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        def is_avl(node):
            if not node:
                return True

            is_cur_balance = abs(get_depth(node.left) - get_depth(node.right)) <= 1
            return is_avl(node.left) and is_avl(node.right) and is_cur_balance

        return is_avl(root)
    

### WITH MEMO
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # is_avl()
        # def get_depth()
        # abs(left_d - right_d) <= 1 and is_avl(node.left) and is_avl_node.right

        memo = {}
        def get_depth(node):
            if node in memo:
                return memo[node]
            if not node:
                return 0
            
            memo[node] = max(get_depth(node.left), get_depth(node.right)) + 1
            return memo[node]

        def is_avl(node):
            if not node:
                return True

            is_cur_balance = abs(get_depth(node.left) - get_depth(node.right)) <= 1
            return is_avl(node.left) and is_avl(node.right) and is_cur_balance

        return is_avl(root)