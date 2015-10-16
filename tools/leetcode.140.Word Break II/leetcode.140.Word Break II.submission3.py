class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        l = len(s)
        dp = [False] * (l+1)
        dp[0] = True
        for i in range(l):
            for w in dict:
                if dp[i] and i+len(w) <= l and w == s[i:i+len(w)]:
                    dp[i+len(w)] = True
        if not dp[-1]: return []

        res = []
        cur = []
        self.helper(s,dict,cur,res)
        return res
        
    def helper(self,s,dict,cur,res):
        if not s:
            res += [' '.join(cur)]
            return
        for i in dict:
            if i == s[:len(i)]:
                cur += [i]
                self.helper(s[len(i):],dict,cur,res)
                del cur[-1]
                
        