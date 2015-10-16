class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n > 0:
            if n % 26 == 0:
                res = 'Z' + res
                n -= 26
            else:
                res = chr(64 + n % 26) + res
            n //= 26
        return res