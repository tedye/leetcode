class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1/x
        res = 1
        base = x
        while n:
            if n & 1:
                res *= base
            n >>= 1
            base *= base
        return res