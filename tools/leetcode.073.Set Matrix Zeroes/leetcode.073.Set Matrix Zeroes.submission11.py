class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix:
            return
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        rows = []
        cols = []
        for i in range(nrow):
            for j in range(ncol):
                if not matrix[i][j]:
                    rows.append(i)
                    cols.append(j)
                
        for row in rows:
            matrix[row] = [0] * ncol
            
        for col in cols:
            for i in range(nrow):
                matrix[i][col] = 0
        