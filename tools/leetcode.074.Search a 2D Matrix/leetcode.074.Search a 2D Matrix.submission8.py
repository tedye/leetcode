class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        if target < matrix[0][0] or target > matrix[len(matrix)-1][len(matrix[0])-1]:
            return False

        for row in matrix:
            if row[0] <= target <= row[-1]:
                if target in row:
                    return True
        return False
