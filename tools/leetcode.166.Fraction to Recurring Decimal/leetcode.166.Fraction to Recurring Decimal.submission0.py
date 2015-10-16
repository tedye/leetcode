class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return ''
        if numerator == 0:
            return '0'
        
        sign = (numerator > 0) ^ (denominator > 0)
        n = abs(numerator)
        d = abs(denominator)
        res = str(n // d)
        n %= d
        if n != 0:
            res += '.'
        dic = {}
        n *= 10
        while n:
            if n not in dic:
                dic[n] = len(res)
                res += str(n//d)
                n %=d
                n *= 10
            else:
                res = res[:dic[n]]+'('+res[dic[n]:]+')'
                break
        if sign:
            return '-'+res
        else:
            return res