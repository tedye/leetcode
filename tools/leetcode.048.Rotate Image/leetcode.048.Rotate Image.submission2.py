class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        cpy = [[0 for i in range(len(matrix))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                cpy[j][-1-i] = matrix[i][j]
        matrix[:] = cpy[:]
    