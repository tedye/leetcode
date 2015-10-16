class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if row[0] <= target <= row[-1]:
                if target in row:
                    return True
        return False
