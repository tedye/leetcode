class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if not nums: return 0
        nums.sort()
        diff = 0x7fffffff
        result = 0
        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums)-1
            while start<end:
                m = nums[i]+nums[start]+nums[end]
                if abs(m - target) < diff:
                    result = m
                    diff = abs(m - target)
                
                if m <= target:
                    start += 1
                else:
                    end -= 1
        return result
                