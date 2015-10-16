class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if not nums: return 1
        i = 0
        l = len(nums)
        while i < l:
            while nums[i] != i+1 and 1<= nums[i] <= l and nums[nums[i]-1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp
            i += 1
        for i in range(l):
            if nums[i] != i+1: return i+1
        return l+1
        