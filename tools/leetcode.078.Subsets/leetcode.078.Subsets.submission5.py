class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res += [sorted(j+[i]) for j in res]
        return res