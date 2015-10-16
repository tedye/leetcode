class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        temp = nums[:]
        while 1:
            left = []
            right = []
            pivot = temp[-1]
            for i in temp[:-1]:
                if i > pivot:
                    left.append(i)
                else:
                    right.append(i)
            if len(left) == k-1:
                return pivot
            elif len(left) < k-1:
                k = k-len(left)-1
                temp = right
            else:
                temp = left
                