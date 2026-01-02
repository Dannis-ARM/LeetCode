# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        dummy = ListNode(0, head)

        i = dummy 
        j = head

        while j is not None:
            next_j = j.next # head 1

            j.next = i # head -> dummy
            i = j
            j = next_j
        
        head.next = None
        return i
    
#### or
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        def reverse(node):
            if node is None:
                return None
            
            if node.next is None:
                return node
            
            new_head = reverse(node.next)
            
            node.next.next = node
            node.next = None
            return new_head
            
        return reverse(head)
    
### my own
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        # dummy = ListNode(val, head)
        ans = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return ans
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        end = head
        while end.next:
            end = end.next

        def reverse_list(start, end):
            i = None
            j = start
            
            stop = end.next
            while j != stop:
                next_j = j.next
                j.next = i
                i = j
                j = next_j
            return i, start # new start, new end
        
        start, end = reverse_list(head, end)
        return start