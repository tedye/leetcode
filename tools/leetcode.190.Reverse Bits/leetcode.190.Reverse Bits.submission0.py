class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = 0
        i = 0
        while i < 32:
            t <<= 1
            t |= (n & 1)
            n >>= 1
            i += 1
        return t