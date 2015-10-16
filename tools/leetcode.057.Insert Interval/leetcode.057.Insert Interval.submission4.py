class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals) == 0: return [newInterval]
        intervals = [Interval(-0x7fffffff,-0x7fffffff)] + intervals + [Interval(0x7fffffff,0x7fffffff)]
        # position of covered intervals in the given intervals
        Sin = None
        Spos = -1
        Ein = None
        Epos = -1
        start = newInterval.start
        end = newInterval.end
        flag1 = False
        flag2 = False
        for i in range(1,len(intervals)):
            if intervals[i].start > start and Spos < 0:
                Spos = i
                Sin = start
                flag1 = True
            elif start <= intervals[i].end and Spos < 0:
                Spos = i
                Sin = intervals[i].start
            if intervals[i].start > end:
                Epos = i
                Ein = end
                flag2 = True
                break
            if intervals[i].end >= end:
                Epos = i
                Ein = intervals[i].end
                break

        if not (flag1 and flag2 and Spos == Epos):
            if flag2:
                for i in range(Spos,Epos):
                    del intervals[Spos]
            else:
                for i in range(Spos,Epos+1):
                    del intervals[Spos]

        return intervals[1:Spos] + [Interval(Sin,Ein)] + intervals[Spos:-1]