class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        res = []
        carry = 1
        for i in digits[::-1]:
            sum = i+carry
            carry = sum // 10
            sum %= 10
            res = [sum] + res
        if carry > 0:
            res = [carry] +  res
        return res
        
        
            