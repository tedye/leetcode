class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1+l2 != l3:
            return False
        dp = [False] * (l2+1)
        dp[0] = True
        for i in range(l2):
            if s2[i] == s3[i]:
                dp[i+1] = dp[i]
        for i in range(l1):
            dp[0] = dp[0] and s1[i] == s3[i]
            for j in range(l2):
                dp[j+1] = dp[j] and s2[j] == s3[i+j+1] or dp[j+1] and s1[i] == s3[i+j+1]
                
        return dp[-1]