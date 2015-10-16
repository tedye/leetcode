class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        if not nums: return []
        d = {}
        for i in range(len(nums)): 
            if (target - nums[i]) in d:
                return [d[target-nums[i]]+1,i+1]
            d[nums[i]] = i
    