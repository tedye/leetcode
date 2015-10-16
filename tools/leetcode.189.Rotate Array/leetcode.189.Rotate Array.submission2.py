class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        l = len(nums)
        k %= l
        nums[:] = nums[-k:] + nums[:-k]
        
        