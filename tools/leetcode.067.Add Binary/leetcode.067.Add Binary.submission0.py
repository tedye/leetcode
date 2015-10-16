class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        la = list(a)
        lb = list(b)
        res = ''
        while la or lb or carry:
            if la and lb:
                op1 = int(la.pop(-1))
                op2 = int(lb.pop(-1))
                sum = carry + op1 + op2
            elif la:
                op1 = int(la.pop(-1))
                sum = carry + op1
            elif lb:
                op2 = int(lb.pop(-1))
                sum = carry + op2
            else:
                sum = carry
            
            carry = sum // 2
            sum %= 2
            res += str(sum)
        return res[::-1]