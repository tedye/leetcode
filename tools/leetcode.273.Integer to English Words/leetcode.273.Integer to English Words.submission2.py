class Solution(object):
    def __init__(self):
        # d1 stores from one to nineteen
        self.d1 = {0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'} 
        # d2 stores from twenty to ninety
        self.d2 = {0:'',2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
        # d3 stores thousand, etc
        self.d3 = ['Thousand','Million','Billion']
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        result = []
        s = str(num)
        end = len(s)
        while end > 0:
            start = max(end-3,0)
            if start != end:
                result += self.convert1000(s[start:end]),
            end -= 3
        res = result[0]
        for i in range(1,len(result)):
            if result[i]:
                res = result[i] + ' ' + self.d3[i-1] + ' ' + res
        return res.strip()
        
        
    def convert1000(self,num):
        n = int(num)
        print(n)
        if n == 0:
            return ''
        elif 0 < n < 20 :
            return self.d1[int(num)]
        elif 20 <= n <= 99:
            return (self.d2[int(num[-2])]+' '+self.d1[int(num[-1])]).strip()
        else:
            return (self.d1[int(num[0])]+' Hundred '+self.convert1000(num[1:])).strip()
            