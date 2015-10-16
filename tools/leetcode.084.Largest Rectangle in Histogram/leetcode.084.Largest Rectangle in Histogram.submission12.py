class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if not height: return 0
        if len(height) < 3: return max(min(height) * len(height),max(height))
        # record curHeigth index
        stack = []
        maxArea = 0
        i = 0
        height.append(0)
        h = len(height)
        while i < h:
            if not stack or (height[i] > height[stack[-1]]):
                stack.append(i)
            else:
                curH = stack.pop(-1)
                if not stack:
                    maxArea = max(maxArea,height[curH] * i)
                else:
                    maxArea = max(maxArea,height[curH] * (i - stack[-1] -1))
                i-=1
            i+=1
        return maxArea
        