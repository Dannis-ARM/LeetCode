# 原来如此，甚至连count都不需要，只需要比较nums[fast]和nums[slow - 2]，因为：nums[slow - 1]表示最新的被更新的元素，nums[slow - 2] <= nums[slow - 1] <= nums[fast]（这个数组本身是单调不减的，[0, slow - 1]的新结果也是单调不减的，而nums[fast]也肯定大于等于它之前遍历过的下标[0, slow - 1]范围的元素）。
# 如果nums[slow - 2] == nums[slow - 1]，则nums[fast] == nums[slow - 2]就说明已经有2个重复元素了，fast指针处的元素要丢弃；如果nums[slow - 2] < nums[slow - 1]，则nums[fast] != nums[slow - 2]恒成立，说明nums[slow - 1]这个元素还只有一个，可以更新nums[slow] = nums[fast]。
# 还是要找出题目给出的要求和数据的性质的关联啊，我还傻傻地想count应该怎么更新。


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i-2] :
                nums[i] = nums[j]
                i += 1

        return i
