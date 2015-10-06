class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        nums.sort()
        l = len(nums)
        while 1:
            res.append(nums[:])
            n = l-1
            while n > 0 and nums[n - 1] >= nums[n]:
                n -= 1
            if n == 0:
                break
            t = n
            while t < l and nums[n - 1] < nums[t]:
                t += 1
            temp = nums[t-1]
            nums[t-1] = nums[n-1]
            nums[n-1] = temp
            nums[n:] = nums[n:][::-1]
        return res 