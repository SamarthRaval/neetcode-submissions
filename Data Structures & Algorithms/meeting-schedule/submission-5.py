"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        length = len(intervals)
        if length == 0 or length == 1:
            return True

        intervals.sort(key=lambda x:x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, length):
            if heap[-1] <= intervals[i].start:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
            else:
                return False

        return True

