# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get len n
        # n // k -> g_num
        # reverse group by group and connect them

        def reverse_list(start, end):
            i = None
            j = start
            
            stop_node = end.next
            while j != stop_node:
                next_j = j.next
                j.next = i
                i = j
                j = next_j
            return i, start # new start, new end

        if head is None:
            return None

        dummy = ListNode(0, head)
        pre_g_end = dummy
        while True:
            g_end = pre_g_end
            for _ in range(k):
                g_end = g_end.next
                if not g_end:
                    return dummy.next

            next_g_start = g_end.next
            new_g_start, new_g_end = reverse_list(pre_g_end.next, g_end) # 2, 1
            pre_g_end.next = new_g_start
            pre_g_end = new_g_end
            new_g_end.next = next_g_start


