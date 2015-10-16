class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        # 00 for 0, 01 for 1, 11 for 2
        
        one = 0
        two = 0
        for i in nums:
            # 00 -> 01
            temp1 = one | ~one & ~two & i
            # 01 -> 11
            temp2 = two | one & ~two & i
            # 11 -> 00
            temp1 ^= one & two & i
            temp2 ^= one & two & i
            one = temp1
            two = temp2
        
        return one
        