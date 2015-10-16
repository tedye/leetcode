class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        d = {}
        x = {}
        for i in range(l1):
            if s[i] not in d:
                d[s[i]] = t[i] 
            else:
                if d[s[i]] != t[i]:
                    return False
            if t[i] not in x:
                x[t[i]] = s[i]
            else:
                if x[t[i]] != s[i]:
                    return False
        return True
        
        