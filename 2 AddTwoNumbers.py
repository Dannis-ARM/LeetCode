# Definition for singly-linked list.
from json.tool import main
from typing import Optional


# Bruteforce
# Big number problem O(mn)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = [], []
        t1, t2 = l1, l2
        while(t1.next):
            num1.insert(0, t1.val)
            t1 = t1.next
        num1.insert(0, t1.val)
        while(t2.next):
            num2.insert(0, t2.val)
            t2 = t2.next
        num2.insert(0, t2.val)
        val1, val2 = self.arrayTwoNumber(num1), self.arrayTwoNumber(num2)
        resArr = self.numberTwoArray(val1+val2)
        resArr.reverse()

        res = self.arrayTwoLinkedList(resArr)
        return res

    @staticmethod
    def arrayTwoLinkedList(resArr):
        res = ListNode(resArr[0])
        curNode = res
        for i in range(len(resArr)):
            if (i < len(resArr)-1):
                nextNode = ListNode(resArr[i+1])
            else:
                nextNode = None
            curNode.next = nextNode
            curNode = curNode.next
        return res

    @staticmethod
    def arrayTwoNumber(arr):
        res = 0
        length = len(arr)
        for i, n in enumerate(arr):
            res += n * pow(10, length-1-i)
        return res

    @staticmethod
    def numberTwoArray(num):
        res = []
        while(num / 10 >= 1):
            digit = num % 10
            res.insert(0, digit)
            num = int(num/10)
        res.insert(0, num)
        return res


# More Neet O(mn)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # t1, t2 = l1, l2
        res = ListNode()
        curNode = res
        carry = 0
        while(True):
            if (l1 and l2):
                sum = l1.val + l2.val + carry
                carry = int(sum/10)
                curNode.val = sum % 10

                if(carry >= 1 or l1.next or l2.next):
                    nextNode = ListNode()
                    curNode.next = nextNode
                    curNode = curNode.next
                l1 = l1.next
                l2 = l2.next
            elif(l1 and not l2):
                sum = l1.val + carry
                carry = int(sum/10)
                curNode.val = sum % 10

                if (carry >= 1 or l1.next):
                    nextNode = ListNode()
                    curNode.next = nextNode
                    curNode = curNode.next
                l1 = l1.next
            elif(l2 and not l1):
                sum = l2.val + carry
                carry = int(sum/10)
                curNode.val = sum % 10

                if (carry >= 1 or l2.next):
                    nextNode = ListNode()
                    curNode.next = nextNode
                    curNode = curNode.next
                l2 = l2.next
            else:
                if (carry >= 1):
                    curNode.val = carry
                return res

# Short one O(mn)
# More Neet O(mn)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p, q = l1, l2
        curNode = dummy
        carry = 0
        while(p or q):
            x = p.val if (p) else 0
            y = q.val if (q) else 0
            sum = x + y + carry
            carry = int(sum/10)
            curNode.next = ListNode(sum % 10)
            curNode = curNode.next
            if (p):
                p = p.next
            if (q):
                q = q.next
        if (carry >= 1):
            curNode.next = ListNode(carry)
        return dummy.next


if __name__ == "__main__":
    # tst = [1, 2, 3]
    # print(arrayTwoNumber(tst))
    l1 = ListNode(1)
    tmp = ListNode(2)
    l1.next = tmp
    tmp = ListNode(3)
    l1.next.next = tmp

    l2 = ListNode(5)
    tmp = ListNode(6)
    l2.next = tmp
    tmp = ListNode(7)
    l2.next.next = tmp

    s1 = Solution()
    res = s1.addTwoNumbers(l1, l2)
    while(res.next):
        print(res.val)
        res = res.next
    print(res.val)
