"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        length = len(intervals)
        if length == 1 or length == 0:
            return True

        intervals.sort(key = lambda x:x.start)
        end = intervals[0].end

        for i in range(1, length):
            if intervals[i].start < end:
                return False
            else:
                end = intervals[i].end

        return True