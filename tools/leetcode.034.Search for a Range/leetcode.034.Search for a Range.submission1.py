class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums: return [-1,-1]
        left = self.findfloor(nums, target)
        right = self.findceil(nums, target)
        try:
            if nums[left] == target and nums[right] == target:
                return [left, right]
        except:
            pass
        return [-1,-1]
        
    def findfloor(self,nums,target):
        i = 0
        l = len(nums)-1
        while i <= l:
            mid = i + (l-i) // 2            
            if nums[mid] < target:
                i = mid + 1 
            else:
                l = mid - 1
        return i
        
    def findceil(self,nums, target):
        i = 0
        l = len(nums)-1
        while i <= l:
            mid = i + (l-i) // 2            
            if nums[mid] > target:
                l = mid - 1 
            else:
                i = mid + 1
        return l