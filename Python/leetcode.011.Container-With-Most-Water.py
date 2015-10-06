class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        start = 0
        end = len(height)-1
        m = 0
        while start < end:
            if height[start] < height[end]:
                m = max(m,height[start] * (end-start))
                start += 1
            else:
                m = max(m, height[end] * (end-start))
                end -= 1
        return m
        