class Solution:
    # @return a string
    def intToRoman(self, num):
        digits = []
        while num != 0:
            digits.append(num % 10)
            num //= 10
        digits = digits[::-1]
                
        thou = {0:'',1:'M', 2:'MM', 3:'MMM'}
        hund = {0:'',1:'C', 2:'CC', 3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}
        ten = {0:'',1:'X', 2:'XX', 3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
        one = {0:'',1:'I', 2:'II', 3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
                
        if len(digits) == 1:
            return one[digits[0]]
        elif len(digits) == 2:
            return ten[digits[0]] + one[digits[1]]
        elif len(digits) == 3:
            return hund[digits[0]] + ten[digits[1]] + one[digits[2]]
        elif len(digits) == 4:
            return thou[digits[0]] + hund[digits[1]] + ten[digits[2]] + one[digits[3]]
