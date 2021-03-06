class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 5
        cnt = 0
        while n >= base:
            cnt += n // base
            base *= 5
        return cnt