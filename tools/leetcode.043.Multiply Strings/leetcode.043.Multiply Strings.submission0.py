class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        
        res = [0] * (l1+l2)
        n1 = [ord(i) - ord('0') for i in list(num1)[::-1]]
        n2 = [ord(i) - ord('0') for i in list(num2)[::-1]]

        for i, n in enumerate(n1):
            for j, m in enumerate(n2):
                res[i+j] += n * m
        carry = 0
        for i in range(len(res)):
            res[i] += carry
            carry = res[i] // 10
            res[i] %= 10
            res[i] = chr(ord('0')+res[i])
        while res[-1] == '0' and len(res) > 1:
            del res[-1]
        
        return ''.join(res)[::-1]