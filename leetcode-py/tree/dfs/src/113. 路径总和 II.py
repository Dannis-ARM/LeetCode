# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        def dfs(node, pass_nodes):
            nonlocal res
            if not node:
                return
            
            cur_state = [*pass_nodes, node.val]
            if node.left is None and node.right is None:
                if sum(cur_state) == targetSum:
                    res.append(cur_state)
                return 
            
            if node.left:
                dfs(node.left, cur_state)
            if node.right:
                dfs(node.right, cur_state)
        
        pass_nodes = []
        dfs(root, pass_nodes)
        return res
            
### backtracking
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        pass_nodes = []
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return
            
            pass_nodes.append(node.val)
            if node.left is None and node.right is None:
                if sum(pass_nodes) == targetSum:
                    res.append([*pass_nodes])
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            pass_nodes.pop()
        
        dfs(root)
        return res
            