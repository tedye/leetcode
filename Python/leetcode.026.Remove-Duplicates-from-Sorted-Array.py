class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        i = 1
        l = len(nums)
        cur = 0
        while i < l:
            if nums[cur] != nums[i]:
                nums[cur+1] = nums[i]
                cur += 1
            i += 1
        return cur + 1