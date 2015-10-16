# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
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
        