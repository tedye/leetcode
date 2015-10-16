class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        m = max(nums)
        cur = 0
        for i in nums:
            cur = max(cur+i, i)
            m = max(m, cur)
        return m
            