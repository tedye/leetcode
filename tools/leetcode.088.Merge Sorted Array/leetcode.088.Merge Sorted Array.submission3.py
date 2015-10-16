class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        #with extra mem.
        nums1cpy = nums1[::]
        pos1 = 0
        pos2 = 0
        pos = 0
        while pos1<m and pos2<n:
            if nums1cpy[pos1] < nums2[pos2]:
                nums1[pos] = nums1cpy[pos1]
                pos += 1
                pos1+= 1
            else:
                nums1[pos] = nums2[pos2]
                pos += 1
                pos2+= 1
        while pos1 < m:
            nums1[pos] = nums1cpy[pos1]
            pos += 1
            pos1+= 1
        while pos2 < n:
            nums1[pos] = nums2[pos2]
            pos += 1
            pos2+= 1
            