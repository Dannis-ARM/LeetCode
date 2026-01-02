# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # dfs - state is passed node.val
        # have a global map to record all node.val
        # find the max
        if not root:
            return None

        dct = defaultdict(int)
        def dfs(node): # sum of certain node
            nonlocal dct

            if not node:
                return 0

            cur_val = dfs(node.left) + dfs(node.right) + node.val
            dct[cur_val] += 1
            return cur_val

        dfs(root)

        res = []
        max_v = max(dct.values())
        for k, v in dct.items():
            if v == max_v:
                res.append(k)

        return res

### normal dfs + memo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # dfs - state is passed node.val
        # have a global map to record all node.val
        # find the max
        if not root:
            return None

        pass_val = 0
        dct = defaultdict(int)
        memo = dict()
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            dfs(node.right)

            lft = memo.get(node.left, 0)
            rgt = memo.get(node.right, 0)

            k = lft + rgt + node.val
            memo[node] = k

            dct[k] += 1
        
        dfs(root)

        res = []
        max_v = max(dct.values())
        for k, v in dct.items():
            if v == max_v:
                res.append(k)

        return res