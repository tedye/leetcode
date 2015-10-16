class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if len(s1) != len(s2): return False
        if sorted(list(s1)) != sorted(list(s2)):
            return False
        
        if s1 == s2: return True
        
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[-i:],s2[:i]) and self.isScramble(s1[:-i], s2[i:]):
                return True
        return False
        