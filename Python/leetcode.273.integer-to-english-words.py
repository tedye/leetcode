class Solution(object):
    def __init__(self):
        self.lookup = {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", \
                       5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                       10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
                       15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
                       20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", \
                       70: "Seventy", 80: "Eighty", 90: "Ninety"}
        self.unit = ["", "Thousand", "Million", "Billion"]
        
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
            
        res, i = [], 0
        while num:
            cur = num % 1000
            if num % 1000:
                res.append(self.threeDigits(cur, self.unit[i]))
            num //= 1000
            i += 1
        return " ".join(res[::-1])

    def threeDigits(self, num, unit):
        res = []
        if num / 100:
            res = [self.lookup[num / 100] + " " + "Hundred"]
        if num % 100:
            res.append(self.twoDigits(num % 100))
        if unit != "":
            res.append(unit)
        return " ".join(res)
    
    def twoDigits(self, num):
        if num in self.lookup:
            return self.lookup[num]
        return self.lookup[(num / 10) * 10] + " " + self.lookup[num % 10]
            