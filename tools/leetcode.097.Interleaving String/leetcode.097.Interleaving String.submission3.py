class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1+l2 != l3:
            return False
        dp = [False] * (l1+1)
        dp[0] = True
        for i in range(1, l1+1):
            if s1[i-1] == s3[i-1]:
                dp[i] = True
            else:
                break

        for i in range(l2):
            if dp[0] and s2[i] != s3[i]:
                dp[0] = False
            for j in range(l1):
                dp[j+1] = dp[j] and s1[j] == s3[i+j+1] or dp[j+1] and s2[i] == s3[i+j+1]
        return dp[-1]
        