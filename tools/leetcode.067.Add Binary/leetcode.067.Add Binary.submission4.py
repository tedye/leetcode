class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if a == "0":
            return b
        if b == "0":
            return a
        t = {"0":0,"1":1}
        a = a[::-1]
        b = b[::-1]
        a = [t[i] for i in a]
        b = [t[i] for i in b]
        tempa = tempb = 0
        for i in range(len(a)):
            tempa += a[i] * 2 ** i
        for i in range(len(b)):
            tempa += b[i] * 2 ** i
        sum = tempa + tempb
        result = ''
        while sum != 0:
            if sum % 2 == 1:
                result = "1" + result
            else:
                result = "0" + result
            sum //= 2
        return result