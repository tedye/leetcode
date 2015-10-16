class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        if m == 1 or n == 1: return 1
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for j in range(1,n+1):
            dp[1][j] = 1
        
        for i in range(2,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
        