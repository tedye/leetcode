class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [0x7fffffff] * (n+1)
        dp[0] = 0
        for i in range(m):
            for j in range(n):
                dp[j+1] = min(dp[j], dp[j+1]) +  grid[i][j]
            dp[0] = 0x7fffffff
        return dp[-1]
        