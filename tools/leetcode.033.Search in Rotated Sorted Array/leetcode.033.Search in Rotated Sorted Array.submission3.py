class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1
        
        pivot = self.findPivot(nums)
        left = self.bsearch(nums, target, 0, pivot - 1)
        if left != -1:
            return left
        right = self.bsearch(nums, target, pivot, len(nums) - 1)
        return right
        
    def findPivot(self, nums):
        i = 0
        l = len(nums) - 1
        while i < l:
            if nums[i] < nums[l]:
                return i
            mid = i + (l-i) // 2
            if nums[mid] >= nums[i]:
                i = mid + 1
            else:
                l = mid
        if nums[i] < nums[l]:
            return i
        else:
            return l
        
    def bsearch(self,nums, target, s, e):
        while s <= e:
            mid = s + (e-s) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return -1
        