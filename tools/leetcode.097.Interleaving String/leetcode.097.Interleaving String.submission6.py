class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s1)+1) for _ in range(len(s2)+1)]
        dp[0][0] = True
        for i in range(len(s1)):
            if s1[i] == s3[i]:
                dp[0][i+1] = True
            else:
                break
        for i in range(len(s2)):
            if s2[i] == s3[i]:
                dp[i+1][0] = True
            else: 
                break
        for i in range(len(s2)):
            for j in range(len(s1)):
                dp[i+1][j+1] = (dp[i+1][j] and s1[j] == s3[i+j+1] or dp[i][j+1] and s2[i] == s3[i+j+1])
        return dp[-1][-1]
            