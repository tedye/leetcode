class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if not nums: return 0
        l = 0
        g = nums[0]
        for a in nums:
            l = max(a, a+l)
            g = max(l,g)
        return g
        