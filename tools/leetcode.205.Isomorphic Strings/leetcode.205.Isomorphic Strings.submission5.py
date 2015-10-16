class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        #attempt one - dict record
        if len(s) != len(t): 
            return False
        d1 = {}
        d2 = {}
        pos = 0
        
        for i in range(len(s)):
            diff = ord(s[i]) - ord(t[i])
            if s[i] not in d1:
                d1[s[i]] = diff
            elif d1[s[i]] != diff:
                return False
            if t[i] not in d2:
                d2[t[i]] = diff
            elif d2[t[i]] != diff:
                return False
        return True