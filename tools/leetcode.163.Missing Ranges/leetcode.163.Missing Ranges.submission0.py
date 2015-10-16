class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ranges = []
        pre = lower - 1
        
        for i in xrange(len(nums) + 1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]
            
            if cur - pre >= 2:
                ranges.append(self.printRange(pre + 1, cur - 1))
                
            pre = cur
            
        return ranges
    
    def printRange(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)
            