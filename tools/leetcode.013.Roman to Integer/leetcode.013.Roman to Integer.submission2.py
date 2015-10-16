class Solution:
    # @return an integer
    def romanToInt(self, s):
        converted = 0
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':-2,'IX':-2,'XL':-20,'XC':-20,'CD':-200,'CM':-200}
        for i in roman.keys():
            converted += s.count(i) * roman[i]
        return converted