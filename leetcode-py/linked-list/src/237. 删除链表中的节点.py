# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 脑筋急转弯啊, 就是为了让值可以一样是吧
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        