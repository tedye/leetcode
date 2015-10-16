class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        # attempt one
        unique = set(nums)
        length = len(nums)//2
        for item in unique:
            if nums.count(item)>length:
                return item