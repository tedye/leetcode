# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key = lambda x: x.start)
        res = [intervals.pop(0)]
        while intervals:
            cur = intervals.pop(0)
            if res[-1].end < cur.start:
                res.append(cur)
            else:
                res[-1].end = max(res[-1].end, cur.end)
        return res
        