class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if not nums:
            return [[]]
        nums.sort()
        prev = self.subsets(nums[:-1])
        return [i+[nums[-1]] for i in prev]+prev
        
        