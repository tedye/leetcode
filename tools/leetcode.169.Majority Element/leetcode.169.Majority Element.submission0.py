class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u = set(nums)
        l = len(nums) // 2
        for i in u:
            if nums.count(i) > l:
                return i