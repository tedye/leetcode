class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        one = 0
        for i in nums:
            one ^= i
        return one
        