class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # check out of bounds

        # min_cap is a dan diao array
        # l = max(weights)
        # r = sum(weights)
        # k is days

        # def check
        # cnt = 0
        # cap = 0
        # for w in weights
        #   if cap + w > mid:
        #       cap = 0
        #       cnt += 1
        #   else
        #       cap += w
        # return cnt <= k

        # while l < r
        # mid = (l + r + 1) // 2
        # if check() -> r = mid - 1
        # else -> i = mid  
        # return i

        l = max(weights)
        r = sum(weights) 

        def check(mid):
            cnt = 1
            cap = 0
            for w in weights:
                if cap + w > mid:
                    cnt += 1
                    cap = w 
                else:
                    cap += w
            return cnt <= days
        
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        
        return l