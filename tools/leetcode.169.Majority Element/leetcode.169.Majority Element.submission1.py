class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        u = set(nums)
        l = len(nums) // 2
        for i in u:
            if nums.count(i) > l:
                return i