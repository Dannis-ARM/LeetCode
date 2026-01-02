# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：

# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。

# 叶节点 是指没有子节点的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        # dfs - tracerse
        # dfs - pass down cur val
        # for each leaf get the value and sum it up
        def dfs(node, pass_val):
            if node is None:
                return 0

            cur_val = pass_val * 10 + node.val
            
            if node.left is None and node.right is None:
                self.sum += cur_val

            dfs(node.left, cur_val)
            dfs(node.right, cur_val)

        dfs(root, 0)
        return self.sum


### Another way
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_child_nums(self, node):
        if node.left is None and node.right is None:
            return [[node.val]]

        res = []
        if node.left is not None: 
            lft_list = self.get_child_nums(node.left) 

            for nums_list in lft_list:
                nums_list.append(node.val)
                res.append(nums_list)

        if node.right is not None: 
            rgt_list = self.get_child_nums(node.right) 

            for nums_list in rgt_list:
                nums_list.append(node.val)
                res.append(nums_list)
        return res

    def convert_list_to_number(self, lst):
        res = 0 
        for i in range(len(lst)):
            res += 10 ** i * lst[i]
        print(lst)
        return res

    def sumNumbers(self, root) -> int:
        if root is None:
            return 0 
        
        nums_lists = self.get_child_nums(root)

        res = 0
        for lst in nums_lists:
            res += self.convert_list_to_number(lst)
        return res
   
# nicer way to do this
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0

        # dfs - tracerse
        # dfs - pass down cur val
        # for each leaf get the value and sum it up
        def dfs(node, pass_val):
            nonlocal sum

            cur_val = pass_val * 10 + node.val
            
            if node.left is None and node.right is None:
                sum += cur_val

            if node.left:
                dfs(node.left, cur_val)
            if node.right:
                dfs(node.right, cur_val)

        dfs(root, 0)
        return sum
        