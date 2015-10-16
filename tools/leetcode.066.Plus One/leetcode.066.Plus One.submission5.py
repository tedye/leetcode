class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if not digits: return []
        #padding 
        digits = [0] + digits
        end = len(digits) - 1
        carry = 1
        while end > 0:
            sum = digits[end] + carry
            carry = sum // 10
            sum %= 10
            digits[end] = sum
            end -= 1
        if carry:
            digits[end] = carry
            return digits
        else:
            return digits[1:]
            