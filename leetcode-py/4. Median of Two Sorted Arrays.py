from typing import List
# Bruteforce O(m+n)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size_nums1, size_nums2 = len(nums1), len(nums2)
        size_res = size_nums1 + size_nums2
        res_nums = [0] * size_res
        i1 = i2 = i_res = 0
        if (size_nums1 < size_nums2):
            tmp = nums2
            nums2 = nums1
            nums1 = tmp
        size_nums1, size_nums2 = len(nums1), len(nums2)
        while(i2 <= size_nums2 - 1):
            if (i1 <= size_nums1-1 and nums1[i1] < nums2[i2]):
                res_nums[i_res] = nums1[i1]
                i1 += 1
            else:
                res_nums[i_res] = nums2[i2]
                i2 += 1
            i_res += 1
        for i in range(i1, size_nums1):
            res_nums[i_res] = (nums1[i])
            i_res += 1

        mid = int(size_res/2)
        if (size_res) % 2 == 0:
            return (res_nums[mid-1]+res_nums[mid])/2
        else:
            return res_nums[mid]

# Neet Code O(log(m+n))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


if __name__ == "__main__":
    s = Solution()
    a = [1, 3]
    b = [2]
    res = s.findMedianSortedArrays(a, b)
    print(res)
