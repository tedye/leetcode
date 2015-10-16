class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if divisor == 0: return None
        if dividend == 0: return 0
        sign = (dividend > 0)^(divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        remainder = dividend
        res = 0
        while remainder > 0:
            temp = divisor
            c = 1
            while temp <= remainder:
                c <<= 1
                temp <<= 1
            temp >>= 1
            c >>= 1
            remainder -= temp
            res += c
        if not sign:
            return min(res,2147483647)
        else:
            return max(-res,-2147483648)
            