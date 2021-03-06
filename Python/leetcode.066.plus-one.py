class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
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