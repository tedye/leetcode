class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string  
    def __init__(self):
        self.chrToD = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        self.dToChr = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    def multiply(self, num1, num2):
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            basePos = i
            for j in range(len(num2)):
                curPos = basePos+j
                res[curPos] += self.chrToD[num1[-i-1]] * self.chrToD[num2[-j-1]]
        for i in range(len(res)):
            if res[i] > 9:
                t = res[i] // 10
                res[i+1] += t
                res[i] -= t * 10
        result = ''.join([self.dToChr[res[-i-1]] for i in range(len(res))])
        i = 0
        while i < len(result)-1 and result[i] == '0':
            i += 1 
        return result[i:]

        