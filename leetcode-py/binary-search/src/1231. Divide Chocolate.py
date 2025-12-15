# 四、避坑指南：如何避免选错？
# 先明确目标：
# 如果是找具体值 / 存在性：用 while i <= j（闭区间）。
# 如果是找极值 / 边界：用 while i < j（收缩区间）。
# 边界更新与中位数匹配：
# 若用 while i < j 且 i = mid，必须用上中位数（mid = (i + j + 1) // 2），避免死循环。
# 若用 while i < j 且 j = mid，必须用下中位数（mid = (i + j) // 2），避免死循环。
# 测试极端情况：
# 比如数组长度为 1、目标值在数组两端，验证代码是否会死循环或漏解。
# 总结
# i <= j：用于查找具体值 / 存在性，区间是闭区间，每个元素都会被检查，终止时区间为空。
# i < j：用于找极值 / 边界，区间是闭区间或左闭右开，通过收缩区间逼近答案，终止时 i = j 即为答案。
# 选择的核心是匹配你的问题目标和区间更新逻辑，而不是死记硬背写法。


class Solution:
    def solve(self, nums, k):
        if len(nums) < k+1:
            return -1
        
        # get max_min_sum
        l = min(nums)
        r = sum(nums)

        def valid(mid):
            cnt = 0
            cur_sum = 0
            for num in nums:
                if cur_sum + num >= mid:
                    cur_sum = 0
                    cnt += 1
                else:
                    cur_sum += num
            return cnt >= k+1
        
        while l < r:
            mid = (l + r) // 2 + 1
            if valid(mid):
                l = mid
            else:
                r = mid-1

        return l


