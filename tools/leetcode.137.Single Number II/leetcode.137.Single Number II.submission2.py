class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        one = two = 0
        for i in nums:
            nextone = one
            nexttwo = two
            nextone |= i&~one
            nexttwo |= i&~two&one
            x = i&one&two
            one = nextone^x
            two = nexttwo^x
        return one
        