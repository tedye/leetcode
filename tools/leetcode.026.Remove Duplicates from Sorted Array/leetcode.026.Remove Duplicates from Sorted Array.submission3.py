class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums: return 0
        pos = 1
        cur = nums[0]
        while pos < len(nums):
            if nums[pos] == cur:
                del nums[pos]
            else:
                cur = nums[pos]
                pos+=1
        return len(nums)
        