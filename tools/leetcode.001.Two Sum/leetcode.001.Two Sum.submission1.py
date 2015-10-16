class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            if target-n in d:
                return [d[target-n], i + 1]
            else:
                d[n] = i + 1
                