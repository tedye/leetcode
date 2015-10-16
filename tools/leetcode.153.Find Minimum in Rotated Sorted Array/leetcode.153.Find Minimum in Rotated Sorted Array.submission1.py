class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if not nums: return -1
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
                