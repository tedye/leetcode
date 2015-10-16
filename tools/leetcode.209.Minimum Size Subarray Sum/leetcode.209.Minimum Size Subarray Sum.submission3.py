class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        # O(n) approach
        if not nums: return 0
        head = 0
        tail = 0
        end = len(nums)
        minlen = len(nums)
        cur = nums[0]
        while head < end:
            while cur < s:
                head += 1
                if head == end:
                    break
                cur += nums[head]
            while cur >= s:
                cur -= nums[tail]
                tail += 1
            minlen = min(head - tail + 2, minlen)
        if minlen == len(nums):
            return 0
        else:
            return minlen
            
            
            
            