class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        n = len(nums)-1
        while n > 0 and nums[n-1] >= nums[n]:
            n -= 1
        t = n
        if t == 0:
            nums[:] = nums[::-1]
            return
        x = nums[n-1]
        while t < len(nums) and x < nums[t]:
            t += 1
        temp = nums[t-1]
        nums[t-1] = nums[n-1]
        nums[n-1] = temp
        nums[n:] = nums[n:][::-1]
        return