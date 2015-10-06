class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        nums.sort()
        res.append(nums[:])
        while 1:
            n = len(nums) - 1
            while n > 0 and nums[n-1] > nums[n]:
                n -= 1
            t = n
            if t == 0: break
            while t < len(nums) and nums[n-1] < nums[t]:
                t += 1
            t -= 1
            temp = nums[n-1]
            nums[n-1] = nums[t]
            nums[t] = temp
            nums[n:] = nums[n:][::-1]
            res.append(nums[:])
        return res