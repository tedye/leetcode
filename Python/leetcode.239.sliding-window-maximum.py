class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        if k > len(nums):
            return [max(nums)]
        d = []
        result = []
        for i in range(k):
            while d and nums[d[-1]] <= nums[i]:
                d.pop(-1)
            d.append(i)
        
        for i in range(k, len(nums)):
            result.append(nums[d[0]])
            while d and d[0] <= i - k:
                d.pop(0)
            while d and nums[d[-1]] <= nums[i]:
                d.pop(-1)
            d.append(i)
        result.append(nums[d[0]])
        return result