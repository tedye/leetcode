class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        if len(nums) < 2: return []
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i+1]
            else:
                d[nums[i]] += [i+1]

        for i in d:
            if target-i in d:
                return sorted([d[i][0],d[target-i][-1]])
        