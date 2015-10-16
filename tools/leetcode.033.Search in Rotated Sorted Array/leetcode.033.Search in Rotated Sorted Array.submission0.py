class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
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
        if len(nums) == 1:
            return 0
        i = 0
        l = len(nums)
        while l - i > 1:
            mid = i + (l - i) // 2
            if nums[mid-1] > nums[mid]:
                return mid
            if nums[i] > nums[mid]:
                l = mid
            else:
                i = mid
        return i
        
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