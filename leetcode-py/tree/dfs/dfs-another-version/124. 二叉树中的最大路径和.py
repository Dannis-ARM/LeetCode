"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = list()
        res.append(-float("inf"))

        def dfs(node, res):
            '''
            get current max value which has pass through this node
            '''
            if node is None:
                return 0
            if node.left is None and node.right is None:
                res[0] = max(node.val, res[0])
                return node.val
           
            left_val = max(dfs(node.left, res), 0)
            right_val = max(dfs(node.right, res), 0)
            max_passable_val = max(left_val, right_val) + node.val

            max_cur_val = right_val + left_val + node.val
            res[0] = max(max_cur_val, res[0])
            return max_passable_val
        
        dfs(root, res)

        return res[0]
        


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
    

# nicer solution
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            # 尽管根据题目约束，root不会是None，但通常这样处理
            return 0 

        # 直接定义一个普通的变量
        max_sum = -float("inf")

        def dfs(node):
            # 声明要修改的是外部作用域的 max_sum 变量
            nonlocal max_sum 
            
            if node is None:
                return 0
            
            left_val = max(dfs(node.left), 0)
            right_val = max(dfs(node.right), 0)
            
            # 更新全局最大值 (max_sum)
            current_path_sum = node.val + left_val + right_val
            max_sum = max(max_sum, current_path_sum)
            
            # 返回当前节点能向上父节点提供的最大单边贡献
            max_passable_val = node.val + max(left_val, right_val)
            return max_passable_val
        
        dfs(root)

        return max_sum