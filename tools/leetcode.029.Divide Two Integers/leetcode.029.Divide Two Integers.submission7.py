class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if not divisor: return None
        if not dividend: return 0
        
        sign = (dividend * divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend > 0:
            temp = divisor
            c = 1
            while temp <= dividend:
                temp <<= 1
                c <<= 1
            temp >>= 1
            c >>= 1
            dividend -= temp
            res += c
        if sign:
            return min(res,2147483647)
        else:
            return max(-res,-2147483648)
            