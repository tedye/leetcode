class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s: return []
        
        cur = []
        res = []
        self.dfs(s,cur,res)
        return res
    
    def dfs(self,s,cur,res):
        if s == "":
            res.append(cur[:])
        else:
            for i in range(len(s)):
                if self.isP(s[:i+1]):
                    cur.append(s[:i+1])
                    self.dfs(s[i+1:],cur,res)
                    del cur[-1]
    
    def isP(self,s):
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
            
                