# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find node
        # update node
        
        ### for update func - chose right side child to replace
        # if replaced_node has two childs
        # new_node = replaced_node.right
        # new_node.leftest_node.left = replaced_node.left
        # if right
        # replaced_node.parent.right = new_node
        # if left
        # replaced_node.parent.left = new_node

        # if replaced_node only has left child
        # if right
        # replaced_node.parent.right = replaced_node.left
        # if left
        # replaced_node.parent.left = replaced_node.left

        # if replaced_node only has right child
        # if right
        # replaced_node.parent.right = replaced_node.right
        # if left
        # replaced_node.parent.left = replaced_node.right

        # if replaced_node has no child
        # if right
        # replaced_node.parent.right = None
        # if left
        # replaced_node.parent.left = None

        def find_node(node, target, parent, right_dir):
            if not node:
                return None, parent, right_dir
            if node.val == target:
                return node, parent, right_dir
            
            if target > node.val:
                return find_node(node.right, target, node, True)
            else:
                return find_node(node.left, target, node, False)
        
        def move_to_leftest(node):
            assert node is not None

            leftest = new_node = node.right
            if new_node is None:
                return node.left

            while leftest.left is not None:
                leftest = leftest.left
            leftest.left = node.left
            return new_node

        if not root:
            return None

        replaced_node, parent, right_dir = find_node(root, key, None, None)
        if not replaced_node:
            return root

        if replaced_node == root:
            return move_to_leftest(root)

        if replaced_node.left is None and replaced_node.right is None:
            if right_dir:
                parent.right = None
            else:
                parent.left = None
        
        if replaced_node.left is not None and replaced_node.right is None:
            if right_dir:
                parent.right = replaced_node.left
            else:
                parent.left = replaced_node.left
        
        if replaced_node.right is not None and replaced_node.left is None:
            if right_dir:
                parent.right = replaced_node.right
            else:
                parent.left = replaced_node.right
        
        if replaced_node.right is not None and replaced_node.left is not None:
            new_node = move_to_leftest(replaced_node)
            # leftest = new_node = replaced_node.right
            # while leftest.left is not None:
            #     leftest = leftest.left
            # leftest.left = replaced_node.left

            if right_dir:
                parent.right = new_node
            else:
                parent.left = new_node
        
        return root
    

### dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # val check
        # three cases

        # for val = key
        # root 4 cases
        # 1 has no child
        # return None
        # 2 not exits
        # return None
        # 3 has one left leaf
        # 4 has one right
        # 5 has two leaves
        def delete_node(node, key):
            if not node:
                return None

            if key == node.val:
                if node.left is None and node.right is None:
                    return None
                if node.left and node.right:
                    leftest = node.right
                    while leftest.left:
                        leftest = leftest.left
                    leftest.left = node.left
                    return node.right
                else:
                    return node.right if node.right else node.left  
                
            if key > node.val:
                node.right = delete_node(node.right, key)
            else:
                node.left = delete_node(node.left, key)
            return node

        return delete_node(root, key)