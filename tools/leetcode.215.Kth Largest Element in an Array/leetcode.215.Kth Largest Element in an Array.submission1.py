class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        while nums:
            pivot = nums.pop(-1)
            left = []
            right = []
            for n in nums:
                if n > pivot:
                    left.append(n)
                else:
                    right.append(n)
            if len(left) == k - 1:
                return pivot
            elif len(left) < k - 1:
                k -= len(left)+1
                nums = right
            else:
                nums = left
        