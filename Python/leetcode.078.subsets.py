class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums.sort()
        prev = self.subsets(nums[:-1])
        return [i+[nums[-1]] for i in prev]+prev
