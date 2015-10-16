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
                res[curPos] += (ord(num1[-i-1])-48) * (ord(num2[-j-1])-48)
                if res[curPos] > 9:
                    t = res[curPos] // 10
                    res[curPos+1] += t
                    res[curPos] -= t * 10

        result = ''
        for i in res:
            result = chr(i+48)+result
        i = 0
        while i < len(result)-1 and result[i] == '0':
            i += 1 
        return result[i:]
        