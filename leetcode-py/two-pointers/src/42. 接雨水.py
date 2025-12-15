class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        i = 1
        j = len(height) - 2
        i_max = height[0]
        j_max = height[len(height)-1]

        sum = 0
        while ( i < j ):
            if i_max < j_max:
                sum += max(i_max - height[i], 0)
                i_max = max(i_max, height[i])
                i += 1
            else:
                sum += max(j_max - height[j], 0)
                j_max = max(j_max, height[j])
                j -= 1
        
        if i == j:
            sum += max(min(i_max, j_max) - height[i], 0)
        
        return sum

### cleaner
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        i = 0
        j = len(height) - 1
        i_max = height[0]
        j_max = height[-1]

        sum = 0
        while ( i < j ):
            if i_max < j_max:
                i += 1
                sum += max(i_max - height[i], 0)
                i_max = max(i_max, height[i])
            else:
                j -= 1
                sum += max(j_max - height[j], 0)
                j_max = max(j_max, height[j])
        return sum

### brute force
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        # sum = 0
        # for i in every ele:
        # find left max and right max
        # sum += max(min(l_max, r_max) - h[i], 0)

        sum  = 0
        for i in range(1, len(height)-1):
            l_max = max(height[:i])
            r_max = max(height[i+1:])
            sum += max(min(l_max, r_max) - height[i], 0)
        return sum