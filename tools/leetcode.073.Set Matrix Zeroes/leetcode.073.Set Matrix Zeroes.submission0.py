class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        col = [False] * n
        row = [False] * m
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col[j] = True
                    row[i] = True
        
        for i in range(m):
            for j in range(n):
                if col[j] or row[i]:
                    matrix[i][j] = 0