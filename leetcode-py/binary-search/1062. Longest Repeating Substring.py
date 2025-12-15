# Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.
# 二分查找的核心是将问题的解空间映射为一个有序的布尔序列，即：
# 存在一个阈值 k，使得所有小于等于 k 的值都满足某个条件，所有大于 k 的值都不满足（或反之）。



# 对于子串长度 L，条件 “存在长度为 L 的重复子串” 具有单调性 —— 若 L 可行，则所有更小的长度都可行；若 L 不可行，则所有更大的长度都不可行。这种单调性使得解空间呈现出有序的布尔序列，恰好匹配二分查找的适用条件。
class Solution:
    def solve(self, s: str):

        # l is 0
        # r is len(s) - 1 because max number of substring 

        # check func
        # check if certain amount of substring exists

        # while l < r
        # mid = (l + r + 1) // 2
        # if exits
            # res = mid
            # l = mid
        # else
            # r = mid - 1
        res = 0
        
        l = 0
        r = len(s) - 1

        def check(mid):
            substring_set = set()
            for i in range(0, len(s)-mid+1):
                substring = s[i:i+mid]
                if substring in substring_set:
                    return True
                substring_set.add(substring)
            return False
                
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                res = mid
                l = mid
            else:
                r = mid - 1
        return res
         
        