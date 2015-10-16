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
        if not intervals: return [newInterval]
        if newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        if newInterval.start > intervals[-1].end:
            return intervals+[newInterval]
        
        beginval =0
        endval = 0
        temp = intervals + [newInterval]
        temp.sort(key=lambda x: x.start)
        s = temp.index(newInterval)
        if s > 0:
            if temp[s-1].end >= temp[s].start:
                s -= 1
        beginval = temp[s].start
        
        temp.sort(key=lambda x: x.end)
        e = temp.index(newInterval)
        if e != len(intervals):
            if temp[e+1].start <= temp[e].end:
                e += 1
        endval = temp[e].end
        return temp[:s] + [Interval(beginval,endval)] + temp[e+1:]
        