class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            x = nums[mid]
            if x == target:
                return True
            if x == nums[l]:
                l += 1
            elif x < nums[l]:
                if x < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < x:
                    r = mid - 1
                else:
                    l = mid + 1
                
        return False