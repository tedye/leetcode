class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        d1 = set()
        d2 = set()
        for i in s:
            if i not in d1:
                d1.add(i)
        for i in dict:
            for j in i:
                if j not in d2:
                    d2.add(j)
        if d1-d2:
            return []
            
        res = []
        cur = []
        self.helper(s,dict,cur,res)
        return res
        
    def helper(self,s,dict,cur,res):
        if s in dict:
            cur += [s]
            res += [' '.join(cur)]
            del cur[-1]
        for i in dict:
            if i == s[:len(i)]:
                cur += [i]
                self.helper(s[len(i):],dict,cur,res)
                del cur[-1]
                
        