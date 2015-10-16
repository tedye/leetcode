class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        curMax = 1
        curMin = 1
        m = nums[0]
        for i in nums:
            temp = curMax
            curMax = max(i,max(curMax*i,curMin*i))
            curMin = min(i,min(curMin*i,temp*i))
            m = max(m, curMax)
        return m
        