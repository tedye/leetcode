class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or k <= 0: 
            return False
        if len(nums) <= k+1:
            return len(set(nums)) != len(nums)
        size = 0
        workingset = set()
        for ind,i in enumerate(nums):
            if i in workingset:
                return True
            if size < k:
                workingset.add(i)
                size += 1
            else:
                workingset.remove(nums[ind - k])
                workingset.add(i)
        return False