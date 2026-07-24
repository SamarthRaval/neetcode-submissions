"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        length = len(intervals)
        heap = []
        if length == 0:
            return 0
        if length == 1:
            return 1

        intervals.sort(key=lambda x:x.start)
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, length):
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, intervals[i].end)

        return len(heap)