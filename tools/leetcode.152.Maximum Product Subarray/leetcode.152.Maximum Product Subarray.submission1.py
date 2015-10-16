class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if not nums: return 0
        maxPositive = 1
        maxNegative = 1
        m = nums[0]
        for i in nums:
            temp = maxPositive
            maxPositive = max(i, max(i*maxPositive, i*maxNegative))
            maxNegative = min(i, min(i*temp, i*maxNegative))
            m = max(m,maxPositive)
        return m
        