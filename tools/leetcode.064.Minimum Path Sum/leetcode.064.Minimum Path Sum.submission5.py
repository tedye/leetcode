class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0: return 0
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for j in range(2,n+1):
            dp[0][j] = 0x7fffffff
        for i in range(2,m+1):
            dp[i][0] = 0x7fffffff
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        
        return dp[-1][-1]
        
        