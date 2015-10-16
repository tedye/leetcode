class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
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
                    
        