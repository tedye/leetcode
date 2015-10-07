class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return len(nums)
        
        counter = 1
        cur = nums[0]
        pos = 1
        while pos < len(nums):
            if nums[pos] == cur:
                if counter < 2:
                    counter += 1
                    pos += 1
                elif counter == 2:
                    del nums[pos]
            else:
                cur = nums[pos]
                counter = 1
                pos += 1
        return len(nums)