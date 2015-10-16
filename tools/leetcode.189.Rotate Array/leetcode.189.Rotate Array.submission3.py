class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if not nums or k == 0:
            return
        k = len(nums) - k%len(nums)
        for i in range(k):
            nums.append(nums.pop(0))