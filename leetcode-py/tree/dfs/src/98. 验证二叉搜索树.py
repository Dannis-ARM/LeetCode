# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node, pass_nodes):
            if not node:
                return 

            if node.left:
                inorder(node.left, pass_nodes)
            pass_nodes.append(node.val)
            if node.right:
                inorder(node.right, pass_nodes)
        
        pass_nodes = []
        inorder(root, pass_nodes)

        for i in range(len(pass_nodes) - 1):
            if pass_nodes[i] >= pass_nodes[i+1]:
                return False
        return True

                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_bst(node, min_limit, max_limit):
            if not node:
                return True
            if node.val >= max_limit or node.val <= min_limit:
                return False
            
            return is_bst(node.left, min_limit, node.val) and is_bst(node.right, node.val, max_limit)
        
        return is_bst(root, -float('inf'), float('inf'))
            
                
### backtracking 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        min_limit = -float('inf')
        max_limit = float('inf')
        def is_bst(node):
            nonlocal min_limit
            nonlocal max_limit

            if not node:
                return True
            if node.val >= max_limit or node.val <= min_limit:
                return False
            
            ori_max_limit = max_limit
            max_limit = node.val
            lft_is = is_bst(node.left)
            max_limit = ori_max_limit

            ori_min_limit = min_limit 
            min_limit = node.val 
            rgt_is = is_bst(node.right)
            min_limit = ori_min_limit

            return lft_is and rgt_is
        
        return is_bst(root)
            
                