class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if not nums: return []
        res = []
        nums.sort()
        while 1:
            n = len(nums)-1
            res.append(nums[:])
            while n > 0 and nums[n-1] >= nums[n]:
                n -= 1
            if n == 0:
                break
            t = n
            while t < len(nums) and nums[t] > nums[n-1]:
                t += 1
            temp = nums[n-1]
            nums[n-1] = nums[t-1]
            nums[t-1] = temp
            
            nums[n:] = nums[n:][::-1]
        return res
            
            