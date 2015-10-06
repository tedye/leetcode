class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if divisor == 0:
            return None
        
        sign = (dividend > 0) ^ (divisor > 0)
        
        de = abs(dividend)
        ds = abs(divisor)
        result = 0
        while de > 0:
            temp = ds
            i = 1
            while de >= temp:
                temp <<= 1
                i <<= 1
            i >>= 1
            temp >>= 1
            result += i
            de -= temp
        if sign:
            return max(-0x7fffffff-1, -result)
        else:
            return min(0x7fffffff, result)