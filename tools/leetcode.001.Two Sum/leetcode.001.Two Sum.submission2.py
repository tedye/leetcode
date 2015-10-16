class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        result = [-1,-1]
        d = {}
        for i,n in enumerate(nums):
            if target - n in d:
                result[0] = d[target - n]
                result[1] = i+1
                break
            else:
                d[n] = i+1
        return result
        