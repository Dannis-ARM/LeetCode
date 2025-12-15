class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        j = len(arr) - 1

        res = -1
        while (i <= j):
            mid = (i + j) // 2 
            if arr[mid] > arr[mid+1]:
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        return res
    
### more standard
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        j = len(arr) - 1

        while (i < j):
            mid = (i + j) // 2 
            if arr[mid] > arr[mid+1]:
                j = mid
            else:
                i = mid + 1
        return i