class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        writep = m+n-1
        while m > 0 or n > 0:
            if m > 0 and n > 0:
                if nums1[m-1] < nums2[n-1]:
                    nums1[writep] = nums2[n-1]
                    n -= 1
                    writep -= 1
                else:
                    nums1[writep] = nums1[m-1]
                    m -= 1
                    writep -= 1
            elif n > 0:
                nums1[writep] = nums2[n-1]
                n -= 1
                writep -= 1
            elif m > 0: break
        