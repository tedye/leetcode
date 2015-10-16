class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return res
        i = 0
        l = len(nums)
        while i < l:
            cur = ''
            start = nums[i]
            cur += str(start)
            i+=1
            while i < l and nums[i] == start+1:
                i += 1
                start += 1
            end = str(nums[i-1])
            if cur == end:
                res.append(cur)
            else:
                res.append(cur+'->'+end)
        return res
        
            