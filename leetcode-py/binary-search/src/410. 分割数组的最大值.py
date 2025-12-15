class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return -1
        # binary search
        # check if get a value that can split the array into k groups and has max minimum 
        # l = max(nums)
        # r = sum
        # use check() to check if current mid (min_max_sum) can valid
        # if true, then it might too big; try new mid = (l+r)/2-1
        # if false, then too small try new mid = (l+r)/2 + 1
        
        # check function def check()
        #  ( try split as less as possbile )
        # check if this need splitted gropus less then ask (cnt <= k)
        # mid (i.e. min_max_sum)
        # starting from cnt = 1 sum = first value
        # for num in nums:
        # if sum += num > mid:
        # cnt +=1 sum = nums[i]
        # else
        # sum += nums[i]
        # return true if cnt <= k else false

        l = max(nums)
        r = sum(nums)
        
        def check(mid):
            sum = 0
            cnt = 1

            for num in nums:
                if (sum + num) > mid:
                    cnt += 1
                    sum = num
                else:
                    sum += num
            return cnt <= k
        
        while l < r:
            mid = (l + r ) // 2        
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l