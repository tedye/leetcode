class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if k == 0: return False
        l = len(nums)
        if l <= k+1:
            return l != len(set(nums))
        
        for i in range(l-k):
            if len(set(nums[i:i+k+1])) != k+1:
                return True
        return False
        