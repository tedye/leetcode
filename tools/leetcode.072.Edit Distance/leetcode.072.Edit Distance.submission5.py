class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        if not word1 and not word2: return 0
        if not word1 and word2 or not word2 and word1: return max(len(word1),len(word2))
        
        dp = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]
        for j in range(len(word1)+1):
            dp[0][j] = j
        for i in range(len(word2)+1):
            dp[i][0] = i
            
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                temp = dp[i-1][j-1]
                if word2[i-1] != word1[j-1]:
                    temp += 1
                dp[i][j] = min(temp, dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[-1][-1]
        