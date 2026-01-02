class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # dfs all nodes - have a state to track current pass
        # if the end node, put the stet into ans
        state = []

        ans = []
        def dfs(nums):
            if len(nums) == 0:
                ans.append([val for val in state])
                return 
            
            for i in range(len(nums)):
                cur = nums[i]
                state.append(cur)
                dfs(nums[:i] + nums[i+1:])
                state.pop()

        dfs(nums)
        return ans