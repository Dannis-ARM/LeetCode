class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        state = []

        ans = []
        def dfs(nums):
            if not nums:
                ans.append([val for val in state])
            picked = set()
            for i in range(len(nums)):
                num = nums[i]
                if num in picked:
                    continue
                picked.add(num)
                
                state.append(num)
                dfs(nums[:i] + nums[i+1:])
                state.pop()
        
        dfs(nums)
        return ans
