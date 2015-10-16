class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        readPos = 0
        writePos = 0
        length = len(nums)
        while readPos < length:
            if nums[readPos] != 0:
                nums[writePos] = nums[readPos]
                writePos += 1
            readPos += 1
        if writePos != length:
            for i in range(writePos, length):
                nums[i] = 0