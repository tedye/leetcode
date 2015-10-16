class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        wkset = [[0] * (len(matrix[0]) + 1) for _ in range(2)]
        prev = 0
        cur = 1
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    wkset[cur][j+1] = 0
                else:
                    wkset[cur][j+1] = min(wkset[prev][j], wkset[prev][j+1], wkset[cur][j]) + 1
                    m = max(m, wkset[cur][j+1])
            cur ^= 1
            prev ^= 1
        return m * m
        