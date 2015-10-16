class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)
        dp = [[False] * (lp+1) for _ in range(ls+1)]
        dp[0][0] = True
        for i in range(1,lp):
            if p[i] == '*':
                dp[0][i+1] = dp[0][i-1]
        
        for i in range(1,ls+1):
            for j in range(1,lp+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # match nothing or match one or match multiple
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j] = dp[i-1][j-1] and p[j-1] == s[i-1]
        return dp[-1][-1]        