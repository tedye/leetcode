class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
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