class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for i in nums:
            res += [j+[i] for j in res if j+[i] not in res]
        return res