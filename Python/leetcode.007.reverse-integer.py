class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x < 0)
        x = abs(x)
        result = 0
        while x:
            result *= 10
            result += x%10
            x //= 10
        if result > 0x7fffffff and not sign or result > 0x7fffffff+1 and sign:
            return 0
        if sign:
            return -1*result
        else:
            return result
