class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        dp0 = dp1 = 1
        for i in range(len(nums)):
            result[i] *= dp0
            result[-i-1] *= dp1
            dp0 = dp0 * nums[i]
            dp1 = dp1 * nums[-i-1]
        return result