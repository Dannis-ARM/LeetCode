# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
            
        # find left node & right node
        # reverse between
        dummy = ListNode(0, head)
        pre_li = dummy

        for _ in range(left-1):
            pre_li = pre_li.next
        
        ri = pre_li
        for _ in range(right-left+1):
            ri = ri.next

        next_ri = ri.next
        li = pre_li.next

        i = None 
        j = li
        while j != next_ri:
            next_j = j.next

            j.next = i
            i = j
            j = next_j

        pre_li.next = i
        li.next = next_ri

        return dummy.next
    
### Second Attempt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre_l = dummy
        for _ in range(left-1):
            pre_l = pre_l.next
        l = pre_l.next

        i = None
        j = l
        for _ in range(right - left + 1):
            next_j = j.next
            j.next = i
            i = j
            j = next_j

        r = i
        l.next = j
        pre_l.next = r

        return dummy.next


