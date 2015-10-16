class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        if not s:
            return []
        # dp[i] means first i letters can be formed by words in the dictionary
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            if dp[i]:
                for word in wordDict:
                    l = len(word)
                    if i+l < len(dp) and s[i:i+l] == word:
                        dp[i+l] = True
        if not dp[-1]: return []
        
        cur = []
        res = []
        self.helper(cur,res, wordDict,s)
        return res
    
    def helper(self, cur, res, d, s):
        if not s:
            res.append(' '.join(cur))
            return
        for word in d:
            l = len(word)
            if l <= len(s) and s[:l] == word:
                cur.append(word)
                self.helper(cur, res, d,s[l:])
                cur.pop(-1)
        
        