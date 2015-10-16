class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if not nums: return 0
        if target > nums[-1]: return len(nums)
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        