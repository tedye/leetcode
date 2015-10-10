class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [0] * 32
        diff = n-m
        mask = 0
        for i in range(32):
            if (m & (1<<i)): 
                limit = 1 << i
                if (m & mask) + diff < limit:
                    res[i] = 1
            mask <<= 1
            mask += 1
        r = 0
        base = 1
        for i in range(32):
            r += res[i] * base
            base *= 2
        return r
            