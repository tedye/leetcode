class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        if not s or len(s) < 4: return []
        res = []
        cur = []
        self.helper(s, res, cur, 0)
        return res
        
    def helper(self, s, res, cur, level):
        if level == 4:
            if not s:
                res.append('.'.join(cur))
            return
        
        if len(s) == 0:
            return
        if len(s) >= 1:
            cur.append(s[0])
            self.helper(s[1:],res,cur,level+1)
            cur.pop(-1)
        if len(s) >= 2 and 10 <= int(s[:2]):
            cur.append(s[:2])
            self.helper(s[2:],res,cur,level+1)
            cur.pop(-1)
        if len(s) >= 3 and 100 <= int(s[:3]) < 256:
            cur.append(s[:3])
            self.helper(s[3:],res,cur,level+1)
            cur.pop(-1)
        