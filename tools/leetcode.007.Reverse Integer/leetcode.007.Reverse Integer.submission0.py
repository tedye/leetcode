class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        # assume the int type is signed and has 4 bytes
        sign = (x < 0)
        res = 0
        temp = x
        if sign:
            temp = -1 * x
        while temp > 0:
            res *= 10
            res += temp%10
            temp //= 10
        if sign:
            res *= -1
        if res > 0x7fffffff or res < -1 * 0x7fffffff - 1:
            return 0
        else:
            return res
            