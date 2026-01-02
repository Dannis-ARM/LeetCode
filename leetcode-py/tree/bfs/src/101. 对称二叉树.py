# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        
        q_lft = [root]
        q_rgt = [root]

        while True:
            if len(q_lft)== 0 and len(q_rgt) == 0:
                return True
            
            if len(q_lft) == 0 or len(q_rgt) == 0:
                return False

            node_lft = q_lft.pop(0)
            node_rgt = q_rgt.pop(0)

            if not node_lft and not node_rgt:
                continue
            
            if not node_lft or not node_rgt:
                return False

            if node_lft.val != node_rgt.val:
                return False
            
            q_lft.append(node_lft.left)
            q_lft.append(node_lft.right)

            q_rgt.append(node_rgt.right)
            q_rgt.append(node_rgt.left)
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(i, j):
            if not i and not j:
                return True
            if not i or not j:
                return False
            if i.val != j.val:
                return False

            return check(i.left, j.right) and check(i.right, j.left)

        return check(root.left, root.right)