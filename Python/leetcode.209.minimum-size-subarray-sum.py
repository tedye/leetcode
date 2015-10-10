class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        start = end = 0
        l = len(nums)
        res = len(nums)
        cur = nums[0]
        while end < l:
            while cur < s:
                end += 1
                if end == l:
                    break
                cur += nums[end]
            while cur >= s:
                cur -= nums[start]
                start += 1
            res = min(res, end - start + 2)
        if res == len(nums):
            return 0
        else:
            return res