class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        r = nums.count(0)
        w = nums.count(1)
        i = 0
        l = len(nums)
        for x in range(r):
            nums[i] = 0
            i+= 1
        for y in range(w):
            nums[i] = 1
            i+= 1
        while i < l:
            nums[i] = 2
            i += 1
        
        
            
        