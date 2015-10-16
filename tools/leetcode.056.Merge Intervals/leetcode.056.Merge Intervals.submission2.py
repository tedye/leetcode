# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals: return []
        temp = sorted(intervals,key=lambda x: x.start)
        res = []
        while temp:
            cur = temp.pop(0)
            if not res or cur.start > res[-1].end:
                res.append(cur)
            else:
                res[-1].end = max(cur.end,res[-1].end)
        return res
        