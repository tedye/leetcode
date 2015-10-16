class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        one = two = 0
        
        for i in nums:
            tempone = one
            one |= (~one&i)
            temptwo = two
            two |= (tempone&(~two)&i)
            x = tempone&temptwo&i
            one ^= x
            two ^= x
        return one
        