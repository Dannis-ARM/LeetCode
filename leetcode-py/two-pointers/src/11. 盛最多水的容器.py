class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        i = 0
        j = len(height)-1

        max_num = -float("inf")
        while (i < j):
            max_num = max(max_num, min(height[j], height[i]) * (j-i))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        
        return max_num