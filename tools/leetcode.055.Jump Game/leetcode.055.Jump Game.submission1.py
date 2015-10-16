class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        x = len(nums)
        if x == 0: return False
        i = 0
        rightb = 0
        while i <= rightb:
            rightb = max(rightb, nums[i]+i)
            i += 1
            if rightb >= len(nums)- 1:
                return True
        return False
        