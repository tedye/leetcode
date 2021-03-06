class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        mask = 1
        i = 0
        while i < 32:
            if n & mask:
                count += 1
            mask <<= 1
            i += 1
            
        return count