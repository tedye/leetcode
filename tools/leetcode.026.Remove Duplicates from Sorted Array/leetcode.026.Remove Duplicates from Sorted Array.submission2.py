class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums: return 0
        pos = 1
        cur = nums[0]
        length = len(nums)
        while pos < length:
            if nums[pos] == cur:
                del nums[pos]
                length -= 1
            else:
                cur = nums[pos]
                pos+=1
        return len(nums)
        