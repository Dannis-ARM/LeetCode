# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        # flag 1 go right (choose right first)
        # flag 0 go left
        
        # for left levet, the parent child right put
        # for right level, the parent, child left put last, others append(0, val)

        if not root:
            return []

        rgt_flag = True
        queue = [root]

        res = []
        while len(queue) != 0:
            queue_len = len(queue)
            
            level = []
            for _ in range(queue_len):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if not rgt_flag:
                level = level[::-1]
            rgt_flag = not rgt_flag
            res.append(level)
        return res
