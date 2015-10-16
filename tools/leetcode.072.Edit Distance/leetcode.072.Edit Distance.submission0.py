class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2: return max(len(word1), len(word2))
        
        dp = [0] * (len(word1)+1)
        for i in range(len(word1)+1):
            dp[i] = i
        
        for i in range(1,len(word2)+1):
            temp = dp[0]
            dp[0] = i
            for j in range(1,len(word1)+1):
                if word1[j-1] != word2[i-1]:
                    temp += 1
                prev = dp[j]
                dp[j] = min(temp, dp[j]+1, dp[j-1]+1)
                temp = prev
        return dp[-1]