class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        if len(height) < 2: return 0
        start = 0
        end = len(height) - 1
        m = 0
        while start < end:
            m = max(m, (end-start)*min(height[start],height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return m
        