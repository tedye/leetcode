class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    
    def helper(self,n):
        if not n:
            return 0
        l = len(n)
        forward = [0] * (l+2)
        backward = [0] * (l+2)
        for i in range(l):
            forward[i+2] = max(forward[i] + n[i], forward[i+1])
            backward[-i-3] = max(backward[-i-1] + n[-i-1], backward[-i-2])
        m = 0
        for i in range(l):
            m = max(forward[i+2] + backward[i+2], m)
        return m