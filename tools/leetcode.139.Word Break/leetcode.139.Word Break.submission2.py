class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return False
        #dp[i] means first i char in s can be broken into words in wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(dp)):
            if not dp[i]:
                continue
            for word in wordDict:
                l = len(word)
                start = i
                end = i + l
                if end >= len(dp) or end < len(dp) and dp[end]:
                    continue
                elif s[start:end] == word:
                    dp[end] = True
        return dp[-1]
        