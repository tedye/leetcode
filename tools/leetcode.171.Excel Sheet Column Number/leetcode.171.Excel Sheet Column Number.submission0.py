class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(s)
        res = 0
        while l:
            cur = l.pop(0)
            res = res * 26 + (ord(cur) - ord('A') + 1)
            
        return res