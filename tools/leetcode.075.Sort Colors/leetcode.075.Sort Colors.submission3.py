class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if not nums: return
        if len(nums) < 5: 
            nums.sort()
            return
    
        red = i = 0
        blue = len(nums)-1

        while i < len(nums):
            if nums[i] == 0:
                temp = nums[red]
                nums[red] = 0
                nums[i] = temp
                red += 1
                i += 1
                continue
            if nums[i] == 2 and i < blue:
                temp = nums[blue]
                nums[blue] = 2
                nums[i] = temp
                blue -= 1
                continue
            i += 1
        
                