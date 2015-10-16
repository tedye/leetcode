class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        res = [[]]
        nums.sort()
        for i in nums:
            res += [j+[i] for j in res]
        return res