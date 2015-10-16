class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s: return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i+1] += dp[i]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
        return dp[-1]
        