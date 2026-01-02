#BF
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = -float("inf")
        for i, h in enumerate(heights):
            l = r = i
            while r + 1 <= len(heights) - 1 and heights[r+1] >= h:
                r += 1
            while l - 1 >= 0 and heights[l-1] >= h:
                l -= 1
            
            max_area = max(max_area, h * (r - l + 1))
        return max_area

# 题解讲得有点复杂，不利于理解。。。说白了，这题考的基础模型其实就是：在一维数组中对每一个数找到第一个比自己小的元素。这类“在一维数组中找第一个满足某种条件的数”的场景就是典型的单调栈应用场景。            
# 太精辟了，其实您说的这个案例才是经典单调栈的场景，仔细一想这道题，无非也是找到最左边第一个低于自己的矩形，和最右边第一个低于自己的矩形，其实这是经典The Next Greater问题，大家可以搜一搜

# without watchers
from collections import defaultdict
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # for each h, find first left and right bar that lower than it
        # then r - l - 1

        # mono stack to find
        # for val that bigger / equal then stack top, push
        # for val lower than stack -> keep pop util its empty or the val cannot be lower anymore 
        
        max_area = -float('inf')

        dct = defaultdict(dict)
        stack = []
        for i, h in enumerate(heights):
            while len(stack) > 0 and h < heights[stack[-1]]:
                dct[stack.pop()]["r"] = i
            stack.append(i)
        while len(stack) != 0:
            dct[stack.pop()]["r"] = len(heights)

        stack = []
        for i in range(len(heights)-1, -1, -1):
            h = heights[i]
            while len(stack) > 0 and h < heights[stack[-1]]:
                dct[stack.pop()]["l"] = i
            stack.append(i)
        while len(stack) != 0:
            dct[stack.pop()]["l"] = -1

        for i in range(len(heights)):
            max_area = max(max_area, (dct[i]["r"] - dct[i]["l"] - 1) * heights[i])
        return max_area


            

