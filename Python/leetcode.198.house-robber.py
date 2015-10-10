class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[0]+nums[2])
        
        length = len(nums)
        temp1 = [0] * (length+2)
        temp2 = [0] * (length+2)
        
        for i in range(len(nums)):
            temp1[i+2] = max(temp1[i]+nums[i],temp1[i+1])
            temp2[length-i-1] = max(temp2[length-i+1]+nums[length-i-1], temp2[length-i])
        
        del temp1[0]
        del temp1[0]
        del temp2[-1]
        del temp2[-1]
        
        m = 0
        for i in range(length-2):
            if m < temp1[i] + temp2[i+2]:
                m = temp1[i] + temp2[i+2]
        return m