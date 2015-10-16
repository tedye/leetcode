class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        x = len(nums)
        if x == 0: return False
        m = 0
        i = 0
        while i <= m:
            m = max(m,i+nums[i])
            if m >= x - 1:
                return True
            i += 1
        return False
        