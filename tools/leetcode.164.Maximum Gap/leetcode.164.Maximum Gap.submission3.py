class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if len(nums) < 2: return 0
        
        i = 0
        while i < 31:
            upper = []
            lower = []
            mask = 1 << i
            for n in nums:
                if n & mask:
                    upper.append(n)
                else:
                    lower.append(n)
            nums = upper + lower
            i += 1
        diff = 0
        for i in range(len(nums)-1):
            diff = max(diff, abs(nums[i] - nums[i+1]))
        return diff
        
        