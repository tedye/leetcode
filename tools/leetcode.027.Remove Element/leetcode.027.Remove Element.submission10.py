class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if not nums: return 0
        pos = 0
        length = len(nums)
        while pos < length:
            if nums[pos] == val:
                del nums[pos]
                length -= 1
            else:
                pos += 1
        return length
        