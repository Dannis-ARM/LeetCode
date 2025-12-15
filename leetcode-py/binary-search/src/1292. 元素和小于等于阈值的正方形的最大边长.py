# only bs
# TODO prefix sum 前缀表

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # find max_min(threshold - k)
        # check() (check square exists)

        l = 0
        r = min(len(mat), len(mat[0]))

        def get_rect(a, b, square_len):
            sum = 0
            for i in range(a, a+square_len):
                for j in range(b, b+square_len):
                    sum += mat[i][j]
            return sum

        def exists(edge_len):
            for i in range(0, len(mat) - edge_len + 1):
                for j in range(0, len(mat[0]) - edge_len + 1):
                    sum = get_rect(i, j, edge_len)
                    if sum <= threshold:
                        return True
            return False

        while l < r:
            mid = (l + r + 1) // 2
            if exists(mid):
                l = mid
            else:
                r = mid - 1
        
        return l
    
# 