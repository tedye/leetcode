class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        res = 0
        line = [0] * len(matrix[0])
        for i in matrix:
            for j in range(len(matrix[0])):
                if i[j] == '0':
                    line[j] = 0
                else:
                    line[j] += 1
            res = max(res,self.largestRectangleArea(line))
        
        return res
        
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