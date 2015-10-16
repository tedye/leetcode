class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        if target > matrix[-1][-1] or target < matrix[0][0]: return False
        M = len(matrix)
        N = len(matrix[0])
        m = 0
        while m < M and matrix[m][0]<= target:
            m += 1
        m -= 1
        
        start = 0
        end = N
        while start < end:
            x = matrix[m][(start+end) // 2]
            if target > x:
                start = (start+end) // 2 + 1
            elif target < x:
                end = (start+end) // 2
            else:
                return True
        return False
        