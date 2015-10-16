class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        res = []
        if len(s) > 12:
            return res
        cur = []
        self.helper(s,cur,res)
        return res
        
    def helper(self,s,cur,res):
        if not s: return
        if len(cur) == 3:
            if int(s) < 256 and s[0] != '0' or s == '0':
                cur += [s]
                res += ['.'.join(cur)]
                del cur[-1]
            return
        
        for i in range(1,4):
            t = s[:i]
            if int(t) < 256:
                cur += [t]
                self.helper(s[i:],cur,res)
                del cur[-1]
            if t[0] == '0':
                break
            