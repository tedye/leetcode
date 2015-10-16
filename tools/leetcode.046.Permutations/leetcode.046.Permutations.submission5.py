class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if not nums: return []
        nums.sort()
        res = []
        res.append(nums[:])
        while 1:
            n = len(nums) - 1
            while n>0 and nums[n-1] > nums[n]:
                t += 1
                n -= 1
            if n == 0:
                break
            t = n
            while t < len(nums) and nums[t]>nums[n-1]:
                t += 1
            if t == len(nums):
                t = -1
            else:
                t -= 1
            temp = nums[n-1]
            nums[n-1] = nums[t]
            nums[t] = temp
            nums[n:] = nums[n:][::-1]
            res.append(nums[:])
        return res
        