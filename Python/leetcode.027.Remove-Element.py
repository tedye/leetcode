class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        while nums and start < len(nums):
            if nums[start] == val:
                del nums[start]
            else:
                start += 1
        return len(nums)