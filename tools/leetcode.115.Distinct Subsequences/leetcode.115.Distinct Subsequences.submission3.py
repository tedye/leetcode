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
            temp = dp[0]
            for j in range(n):
                tmp = dp[j+1]
                if s[i] == t[j]:
                    dp[j+1] += temp
                temp = tmp
        return dp[-1]
        