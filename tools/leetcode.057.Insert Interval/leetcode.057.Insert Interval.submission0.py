# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x.start)
        return self.mergeInterval(intervals)
    
    def mergeInterval(self, intervals):
        res = [intervals.pop(0)]
        while intervals:
            cur = intervals.pop(0)
            if cur.start <= res[-1].end:
                res[-1].end = max(cur.end, res[-1].end)
            else:
                res.append(cur)
            
        return res