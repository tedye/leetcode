class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for i in nums:
            res += [j+[i] for j in res if j+[i] not in res]
        return res
        