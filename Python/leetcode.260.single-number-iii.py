class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        workingset = set()
        for n in nums:
            if n not in workingset:
                workingset.add(n)
            else:
                workingset.remove(n)
        return list(workingset)
        