class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
        if len(nums) == 3: return max(nums[0],nums[1],nums[2])
        a = nums[0]
        temp1 = self.helper(nums[1:])
        temp2 = self.helper(nums[2:len(nums)-1])
        return max(temp1, temp2+a)
        
    def helper(self,nums):
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
        length = len(nums)
        
        temp1 = [0] * (length+2)
        temp2 = [0] * (length+2)
        
        for i in range(length):
            temp1[i+2] = max(temp1[i+1],temp1[i]+nums[i])
            temp2[length-1-i] = max(temp2[length-i], temp2[length+1-i]+nums[length-1-i])
            
        m = 0
        for i in range(length-2):
            if m < temp1[i+2]+temp2[i+2]:
                m = temp1[i+2]+temp2[i+2]
        return m
        