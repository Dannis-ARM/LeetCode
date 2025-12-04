from typing import List
# Bruteforce
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # m, n = 0, 1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]) == target:
                    return [i,j] 
        return None

# Two pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        prevMap = {}
        for i in range(len(nums)):
            prevMap[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in prevMap and prevMap[diff] != i):
                return [i,prevMap[diff]]
        return None

# One pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        prevMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [i, prevMap[diff]]
            prevMap[n] = i
        return None