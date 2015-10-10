class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        i = 0
        while i < 31:
            upper = []
            lower = []
            mask = 1 << i
            for num in nums:
                if num&mask:
                    upper.append(num)
                else:
                    lower.append(num)
            nums = lower +  upper
            i += 1
        m = 0
        for i in range(1, len(nums)):
            m = max(m, nums[i] - nums[i-1])
        return m