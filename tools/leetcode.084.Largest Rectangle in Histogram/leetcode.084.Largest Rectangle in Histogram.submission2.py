class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        if not height: return 0
        height.append(0)
        i = 0
        l = len(height)
        m = 0
        stack = []
        while i < l:
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = stack.pop(-1)
                if not stack:
                    m = max(m, height[h]*i)
                else:
                    m = max(m, height[h]*(i - stack[-1] - 1))
        return m
