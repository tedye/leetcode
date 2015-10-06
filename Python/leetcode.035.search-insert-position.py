class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        if target < nums[0]:
            return 0
        
        l = 0
        r = len(nums)
        while r-l > 1:
            mid = l + (r-l)//2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        if nums[l] == target:
            return l
        else:
            return l+1