class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        start = 0
        while nums and start < len(nums):
            if nums[start] == val:
                del nums[start]
            else:
                start += 1
        return len(nums)
                
        
                
                
                
                