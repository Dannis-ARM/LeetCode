# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# 我们的思路本质是：
# 按会议开始时间排序：确保按时间顺序处理会议，不会跳过早开始的会议先处理晚的（这是时间类问题的基础，保证逻辑的时序性）。
# 用最小堆存储结束时间：堆顶始终是当前所有占用会议室中最早结束的时间（这是局部最优的关键选择）。
# 冲突判断：对于当前会议，若它的开始时间 ≥ 堆顶的结束时间（最早空闲的会议室已空），则复用该会议室；否则新增会议室。
# 这个策略的核心是：每一次都优先使用最早能空出来的会议室，而不是新增会议室—— 这是局部最优的选择，而这种选择能直接导向全局最优（最少会议室）。

import heapq

class Solution:
    def minMeetingRooms(intervals: list[list]):
        intervals.sort()

        min_heap = []
        for interval in intervals:
            l, r = interval

            if len(min_heap) == 0:
                min_heap.append(interval[1])
                continue
            
            if l >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
        return len(min_heap)

