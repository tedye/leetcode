class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or k < 1 or t < 0: return False
        
        d = {}
        for i in range(len(nums)):
            x = nums[i] // (t+1)
            if x in d or x-1 in d and nums[i] - d[x-1] <= t or x+1 in d and d[x+1] - nums[i] <= t:
                return True
            if len(d) == k:
                del d[nums[i-k] // (t+1)]
            d[x] = nums[i]
        return False
        