import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # get frequency of each element On
        # sort the frequency list Oklogk
        # get max k elements 

        # or 
        # On Ok
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            else:
                map[num] += 1
        
        # need use max heap
        heap = []
        for num, count in map.items():
            heapq.heappush(heap, (-count, num))
        
        res = []
        for _ in range(k):
            if len(heap) <= 0:
                break
            cnt, num = heapq.heappop(heap)
            res.append(num)
            
        return res


                


