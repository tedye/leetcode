class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1,n+1):
            dp[i] = sum([dp[x]*dp[i-1-x] for x in range(i)])
        return dp[-1]
        