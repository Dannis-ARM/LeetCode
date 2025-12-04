# reconstruct binary tree

preorder_list
inorder_list

1. get root
2. find root from inorder list - get left side nodes number and right side nodes number 
3. now you can get left side nodes and right side nodes from preorder list 
4. recursively to use left side nodes to get its left tree and right tree

```code
class TreeNode:
    """定义二叉树节点结构"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    
    # 1. 预处理：创建中序序列的值到索引的映射
    # 作用：O(1) 快速定位根节点在中序序列中的位置
    inorder_map = {val: i for i, val in enumerate(inorder)}
    
    def helper(pre_start, pre_end, in_start, in_end):
        """
        递归函数：
        - pre_start, pre_end: 当前子树在前序序列中的范围
        - in_start, in_end: 当前子树在中序序列中的范围
        """
        
        # 递归终止条件：如果范围为空，表示没有子树
        if pre_start > pre_end or in_start > in_end:
            return None

        # 1. 确定根节点
        # 当前子树的根节点是前序序列的第一个元素
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        
        # 2. 在中序序列中定位根节点的位置
        # O(1) 查找
        root_index_in_inorder = inorder_map[root_val]
        
        # 3. 计算左子树的节点数量
        # 左子树节点数 = 根节点在中序序列中的索引 - 中序序列的起始索引
        left_subtree_size = root_index_in_inorder - in_start
        
        # 4. 递归重构左右子树
        
        # 重构左子树:
        root.left = helper(
            # 左子树的前序序列范围: 根节点后开始，长度为 left_subtree_size
            pre_start + 1,
            pre_start + left_subtree_size,
            # 左子树的中序序列范围: in_start 到 根节点前一个位置
            in_start,
            root_index_in_inorder - 1
        )
        
        # 重构右子树:
        root.right = helper(
            # 右子树的前序序列范围: 左子树前序序列结束后开始，到 pre_end
            pre_start + left_subtree_size + 1,
            pre_end,
            # 右子树的中序序列范围: 根节点后一个位置，到 in_end
            root_index_in_inorder + 1,
            in_end
        )
        
        return root

    # 调用递归函数，处理整个树的范围
    n = len(preorder)
    return helper(0, n - 1, 0, n - 1)

# --- 示例运行 ---
preorder_list = [3, 9, 20, 15, 7]
inorder_list = [9, 3, 15, 20, 7]

# 调用重构函数
root_node = buildTree(preorder_list, inorder_list)

# 验证（通过对重构后的树进行中序遍历来验证）
def check_inorder(root):
    """验证函数：对树进行中序遍历并返回结果列表"""
    if not root:
        return []
    return check_inorder(root.left) + [root.val] + check_inorder(root.right)

# 打印验证结果，应与 inorder_list 相同
print(f"重构后的树进行中序遍历的结果: {check_inorder(root_node)}")
# 预期输出: [9, 3, 15, 20, 7]

```