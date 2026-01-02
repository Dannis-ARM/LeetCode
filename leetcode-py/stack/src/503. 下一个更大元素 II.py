from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = max(nums)
        mi = nums.index(m)

        # find nums for [0, mi) - 
        #   nums[0:mi] - extract [0, mi)
        
        # find nums for [mi, n) - [mi, n + mi) 
        #   nums[mi:] + mi[:mi]
        #   extract [mi, n)

        res = deque()
        stack = []
        nums2 = nums + nums[0:mi+1]
        for num in nums2[::-1]:
            while len(stack)!=0 and num >= stack[-1]:
                stack.pop()

            if len(stack) == 0:
                res.appendleft(-1)
            else:
                res.appendleft(stack[-1])
            stack.append(num)

        return list(res)[:n]