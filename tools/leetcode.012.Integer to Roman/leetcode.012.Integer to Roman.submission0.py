class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        t = num // 1000
        if t:
            res += 'M' * t
        
        num %= 1000
        
        h = num // 100
        if h:
            if h == 9:
                res += 'CM'
            elif h >= 5:
                res += 'D'
                h -= 5
                if h:
                    res += 'C' * h
            elif h == 4:
                res += 'CD'
            else:
                res += 'C' * h
            
        num %= 100
        t = num // 10
        if t:
            if t == 9:
                res += 'XC'
            elif t >= 5:
                res += 'L'
                t -= 5
                if t:
                    res += 'X' * t
            elif t == 4:
                res += 'XL'
            else:
                res += 'X' * t
                
        num %= 10
        if num:
                
            if num == 9:
                res += 'IX'
            elif num >= 5:
                res += 'V'
                num -= 5
                if num:
                    res += 'I' * num
            elif num == 4:
                res += 'IV'
            else:
                res += 'I' * num
        
        return res        