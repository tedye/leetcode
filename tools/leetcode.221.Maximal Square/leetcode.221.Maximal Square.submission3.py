class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix: return 0
        
        s = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        m = 0
        for i in range(len(s)):
            s[i][0] = int(matrix[i][0])
            m = max(m, s[i][0])
        for j in range(len(s[0])):
            s[0][j] = int(matrix[0][j])
            m = max(m, s[0][j])
        for i in range(1,len(s)):
            for j in range(1,len(s[0])):
                if matrix[i][j] =='0':
                    s[i][j] = 0
                else:
                    s[i][j] = min(s[i-1][j], s[i-1][j-1], s[i][j-1]) + 1
                    m = max(m,s[i][j])
        return m*m
        