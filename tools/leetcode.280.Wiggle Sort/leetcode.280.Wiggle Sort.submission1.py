class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # first attempt: just mimic bubble sort
        '''    
        n = len(nums) - 1
        for i in range(n+1):
            for i in range(n):
                if i & 1 and nums[i] < nums[i+1] or not i & 1 and nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        print(nums)
        # fail to pass the time limit
        '''
        n = len(nums)
        if n <= 1:
            return
        prev = nums[0]
        for i in range(1,n):
            if i & 1 and prev <= nums[i] or not i&1 and prev >= nums[i]:
                nums[i-1] = prev
                prev = nums[i]
            else:
                nums[i-1],nums[i] = nums[i], nums[i-1]
        print(nums)
        