class Solution(object):    def singleNumber(self, nums):        """        :type nums: List[int]        :rtype: int        """        one = 0        for i in nums:            one ^= i        return one