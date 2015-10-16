# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        m = 0
        length = len(points)
        if length <= 2:
            return length
        for i in range(length):
            dupcnt = 1
            l = {}
            for j in range(length):
                if i != j:
                    if points[i].x == points[j].x and points[i].y == points[j].y:
                        dupcnt += 1
                    elif points[i].x == points[j].x:
                        l['v'] = l.get('v',0) + 1
                    elif points[i].y == points[j].y:
                        l['h'] = l.get('h',0) + 1
                    else:
                        slope = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                        l[slope] = l.get(slope, 0) + 1
            if l:
                m = max(m, max(l.values())+dupcnt)
            else:
                m = max(m, dupcnt)
        return m 