class Solution:    # @param {integer[]} nums    # @return {integer}    def longestConsecutive(self, nums):        if not nums: return 0        nums = list(set(nums))        m = min(nums)        nums = [i - m for i in nums]        i = 0                while i < 31:            mask = (1<<i)            lower = []            upper = []            for n in nums:                if (n&mask)>>i:                    upper.append(n)                else:                    lower.append(n)            nums = lower + upper            i += 1        i = 1        l = len(nums)        m = 1        old = nums[0]        cur = 1        while i < l:            if nums[i] == old:                i += 1                continue            if nums[i] == old+1:                cur += 1            else:                m = max(m, cur)                cur = 1            old = nums[i]            i += 1        return max(m,cur)            