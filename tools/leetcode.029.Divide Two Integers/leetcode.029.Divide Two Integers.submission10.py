class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return
        if dividend == 0:
            return 0
        sign = (dividend * divisor > 0)
        remainder = abs(dividend)
        divisor = abs(divisor)
        cnt = 0
        while remainder > divisor:
            temp = divisor
            c = 1
            while remainder > temp and temp > 0:
                temp <<= 1
                c <<= 1
            temp >>= 1
            c >>= 1
            remainder -= temp
            cnt += c 

        if remainder == divisor:
            cnt += 1
        if sign:
            return cnt
        else:
            return cnt * -1