# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda x: x.start)
        return self.helper(intervals)
    
    def helper(self, intervals):
        if len(intervals) < 2:
            return len(intervals)
        
        nextLayer = []
        prev = 0
        n = 1
        length = len(intervals)
        while n < length:
            if intervals[prev].end > intervals[n].start:
                nextLayer.append(intervals[n])
            else:
                prev = n
            n += 1
        
        return self.helper(nextLayer) + 1
        