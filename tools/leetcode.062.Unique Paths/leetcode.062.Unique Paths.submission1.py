class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        dp = [1] * n
        for i in range(m-1):
            for j in range(1,n):
                dp[j] += dp[j-1]
        return dp[-1]
        