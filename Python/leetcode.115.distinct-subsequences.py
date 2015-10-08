class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if s[i] == t[-j-1]:
                    dp[-j-1] += dp[-j-2]
        return dp[-1]