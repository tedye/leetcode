class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if not matrix: return matrix
        length_n = len(matrix[0])
        length_m = len(matrix)
        newMat = []
        for i in range(length_n):
            temp = []
            for j in range(length_m):
                temp.append(matrix[j][i])
            newMat.append(temp[::-1])
        return newMat
            