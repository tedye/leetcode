class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for j in range(1,n+1):
            if not obstacleGrid[0][j-1]:
                dp[1][j] = 1
            else:
                break
        
        for i in range(2,1+m):
            for j in range(1,1+n):
                if not obstacleGrid[i-1][j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        