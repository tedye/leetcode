class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums += [-1]
        i = 0
        l = len(nums)
        while i < l:
            while nums[i] != -1 and nums[i] != i:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
            i += 1
        return nums.index(-1)