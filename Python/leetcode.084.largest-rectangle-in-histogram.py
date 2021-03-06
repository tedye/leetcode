class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        height.append(0)
        i = 0
        l = len(height)
        stack = []
        maxA = 0
        while i < l:
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = stack.pop(-1)
                if not stack:
                    maxA = max(maxA, height[h] * i)
                else:
                    maxA = max(maxA, height[h] * (i - stack[-1] - 1))
        return maxA