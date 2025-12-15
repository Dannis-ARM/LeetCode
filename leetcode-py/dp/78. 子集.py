class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]], []]

        res = []
        for subnet in self.subsets(nums[1:]):
            res.append(subnet)
            res.append([*subnet] + [nums[0]])
        return res



### Using state 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        cur = []
        def dfs(cur: list, idx):
            if idx > len(nums) - 1:
                res.append([*cur])
                return 

            dfs(cur, idx+1)
            cur.append(nums[idx])
            dfs(cur, idx+1)
            cur.pop()
            return

        dfs(cur, 0)
        return res