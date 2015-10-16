class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        if not height:
            return 0
        if len(height) < 3: return max(min(height) * len(height), max(height))
        height = height + [0]
        stack = []
        i = 0
        l = len(height)
        m = 0
        while i < l:
            if not stack or (height[i] > height[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                cur = stack.pop(-1)
                if not stack:
                    m = max(m,height[cur] * i)
                else:
                    m = max(m, height[cur] *(i - stack[-1]-1))
        return m