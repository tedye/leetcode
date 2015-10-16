class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        if n == 0: return 0

        left = [0] * n
        right = [n] * n
        height = [0] * n
        global_max = 0
        for i in range(m):
            curL = 0
            curR = n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j],curL)
                else:
                    height[j] = 0
                    left[j] = 0
                    curL = j + 1
                if matrix[i][-j-1] == '1':
                    right[-j-1] = min(right[-j-1], curR)
                else:
                    right[-j-1] = n
                    curR = n-j-1
            local_max = max([(right[i]-left[i]) * height[i] for i in range(n)])
            global_max = max(global_max,local_max)
        return global_max