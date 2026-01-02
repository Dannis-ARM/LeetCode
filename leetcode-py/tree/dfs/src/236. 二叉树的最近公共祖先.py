# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        found_path = []
        def get_path(node, paths, target_node):
            nonlocal found_path

            if not node:
                return
            cur_paths = [*paths, node]
            if node == target_node:
                found_path = cur_paths
                return 

            if node.left:
                get_path(node.left, cur_paths, target_node)
            if node.right:
                get_path(node.right, cur_paths, target_node)
            return
            
        found_path = []
        get_path(root, [], p)
        assert len(found_path) != 0
        p_paths = [*found_path]

        found_path = []
        get_path(root, [], q)
        assert len(found_path) != 0
        q_paths = [*found_path]

        if len(p_paths) < len(q_paths):
            p_paths, q_paths = q_paths, p_paths
        
        idx = 0
        while idx <= len(q_paths)-1 and q_paths[idx] == p_paths[idx]:
            idx += 1
        return q_paths[idx-1]
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        found_path = []
        paths = []
        def get_path(node, target_node):
            nonlocal paths
            nonlocal found_path

            if not node:
                return
            paths.append(node)
            if node == target_node:
                found_path = [*paths]
                return 

            if node.left:
                get_path(node.left, target_node)
            if node.right:
                get_path(node.right, target_node)
            paths.pop()
            return
            
        found_path = []
        paths = []
        get_path(root, p)
        assert len(found_path) != 0
        p_paths = [*found_path]

        found_path = []
        paths = []
        get_path(root, q)
        assert len(found_path) != 0
        q_paths = [*found_path]

        if len(p_paths) < len(q_paths):
            p_paths, q_paths = q_paths, p_paths
        
        idx = 0
        while idx <= len(q_paths)-1 and q_paths[idx] == p_paths[idx]:
            idx += 1
        return q_paths[idx-1]