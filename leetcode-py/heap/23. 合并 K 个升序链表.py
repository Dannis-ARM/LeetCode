"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
import itertools

count = itertools.count()

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        heap = []

        # O(nlogk)
        # k = len(lists)

        dummy = cur = ListNode(-1, None)

        for node in lists:
            if node is not None:
                heapq.heappush(heap, (node.val, next(count), node))
        
        while(len(heap) != 0):
            val, _, node = heapq.heappop(heap)

            cur.next = ListNode(val, None)
            cur = cur.next

            next_node = node.next
            if next_node is not None:
                heapq.heappush(heap, (next_node.val, next(count), next_node))
        
        return dummy.next