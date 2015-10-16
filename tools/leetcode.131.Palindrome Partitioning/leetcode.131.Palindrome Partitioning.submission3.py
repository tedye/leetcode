class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s: return []
        cur = []
        res = []
        self.helper(s,res,cur)
        return res
        
    
    def helper(self,s,res,cur):
        if not s:
            res.append(cur[:])
            return
        for i in range(1,len(s)+1):
            if s[:i] == s[:i][::-1]:
                cur.append(s[:i])
                self.helper(s[i:],res,cur)
                cur.pop(-1)
            