class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        if not nums: return []
        d = {}
        for i,num in enumerate(nums):
            if target-num in d:
                return [d[target-num]+1,i+1]
            d[num] = i