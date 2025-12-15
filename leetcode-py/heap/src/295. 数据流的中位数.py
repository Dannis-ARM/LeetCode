import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = list()
        self.max_heap = list()

    def addNum(self, num: int) -> None:
        min_heap = self.min_heap
        max_heap = self.max_heap

        if not max_heap:
            heapq.heappush(max_heap, -num)
            return 

        if num > -max_heap[0]:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -num)

        if len(max_heap) >= len(min_heap) + 2:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) >= len(max_heap) + 2:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

    def findMedian(self) -> float:
        min_heap = self.min_heap
        max_heap = self.max_heap
        if len(min_heap) == len(max_heap):
            return (min_heap[0] + -max_heap[0]) / 2
        elif len(min_heap) > len(max_heap):
            return min_heap[0]
        else:
            return -max_heap[0]
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

