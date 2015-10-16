class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        l = len(nums)
        if l < 2:
            return []
        
        d = {}
        for i, n in enumerate(nums):
            if target-n in d:
                return [d[target-n],i+1]
            d[n] = i+1
        return []