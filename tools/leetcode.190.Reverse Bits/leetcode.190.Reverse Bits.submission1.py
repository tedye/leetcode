class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        t = 0
        i = 0
        while i < 32:
            t <<= 1
            t |= (n & 1)
            n >>= 1
            i += 1
        return t
    