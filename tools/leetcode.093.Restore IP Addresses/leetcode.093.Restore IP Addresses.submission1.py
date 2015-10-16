class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        if len(s) < 4:
            return []
        cur = []
        res = []
        self.helper(s, cur, res, 0)
        return res
        
    def helper(self, s, cur, res, level):
        if level == 4:
            if not s:
                res.append('.'.join(cur))
            return
        
        if not s:
            return 
        
        cur.append(s[0])
        self.helper(s[1:], cur, res, level+1)
        cur.pop(-1)
        
        if len(s) > 1 and 10 <= int(s[0:2]) < 100:
            cur.append(s[0:2])
            self.helper(s[2:], cur, res, level+1)
            cur.pop(-1)
        if len(s) > 2 and 100 <= int(s[0:3]) <= 255:
            cur.append(s[0:3])
            self.helper(s[3:], cur, res, level + 1)
            cur.pop(-1)
        
        
        