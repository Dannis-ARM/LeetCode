# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs
class Solution:
    def dfs(self, cur):
        if cur is None:
            return 0
        return max(self.dfs(cur.left), self.dfs(cur.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

# bfs
class Solution:
    def bfs(self, que: list, height):
        while len(que) != 0:
            height += 1
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left is not None:
                    que.append(cur.left)
                if cur.right is not None:
                    que.append(cur.right)
        return height

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        que = [root]
        return self.bfs(que, 0)