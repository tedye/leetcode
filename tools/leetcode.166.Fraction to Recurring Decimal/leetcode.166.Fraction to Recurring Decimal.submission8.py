class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0: return ''
        if numerator == 0: return '0'

        res = ''
        if (numerator > 0) ^ (denominator > 0):
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        if numerator%denominator == 0: 
            return res+str(numerator//denominator)

        res += str(numerator//denominator)+'.'
        
        remain = (numerator % denominator) * 10
        d = {}
        while remain:
            if remain in d:
                cut = d[remain]
                res = res[:cut] + '('+ res[cut:]+')'
                return res
            else:
                d[remain] = len(res)
                res += str(remain//denominator)
                remain = (remain % denominator) * 10
        return res

        
                
        