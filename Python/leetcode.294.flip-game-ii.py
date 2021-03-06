class Solution(object):
    def __init__(self):
        self.d = {}
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in self.d:
            return self.d[s]
        result = False
        for i in xrange(len(s)-1):
            if s[i:i+2] == '++' and not self.canWin(s[:i]+'--'+s[i+2:]):
                result = True
                break
        self.d[s] = result
        return result
