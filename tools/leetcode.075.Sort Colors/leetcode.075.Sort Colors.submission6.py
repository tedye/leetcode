class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        d = {0:0,1:0,2:0}
        for i in nums:
            d[i] += 1
        d[1] += d[0]
        d[2] += d[1]
        
        for i in range(d[2]):
            if i < d[0]:
                nums[i] = 0
            elif i < d[1]:
                nums[i] = 1
            elif i < d[2]:
                nums[i] = 2
        