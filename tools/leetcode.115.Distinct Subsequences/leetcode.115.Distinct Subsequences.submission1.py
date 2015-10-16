class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if s[i] == t[-j-1]:
                    dp[-j-1] += dp[-j-2]
        return dp[-1]
        