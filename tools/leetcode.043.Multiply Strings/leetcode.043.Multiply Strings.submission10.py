class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string  
    def multiply(self, num1, num2):
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            basePos = i
            for j in range(len(num2)):
                curPos = basePos+j
                res[curPos] += int(num1[-i-1]) * int(num2[-j-1])
                
        for i in range(len(res)):
            if res[i] > 9:
                t = res[i] // 10
                res[i+1] += t
                res[i] -= t * 10
        result = ''
        for i in res:
            result = str(i)+result
        i = 0
        while i < len(result)-1 and result[i] == '0':
            i += 1 
        return result[i:]
        