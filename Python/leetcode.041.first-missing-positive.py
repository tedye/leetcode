class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        
        i = 0
        l = len(nums)
        while i < l:
            while 0 < nums[i] <= l and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
            i += 1
        for i in range(l):
            if nums[i] != i+1:
                return i + 1
        return l+1