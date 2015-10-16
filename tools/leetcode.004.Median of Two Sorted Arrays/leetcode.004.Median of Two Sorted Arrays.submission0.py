class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        length1 = len(nums1)
        length2 = len(nums2)
        length = length1 + length2
        if length & 1:
            return self.helper(nums1, 0, length1-1, nums2, 0, length2-1, length // 2) * 1.0
        else:
            return (self.helper(nums1, 0, length1-1, nums2, 0, length2-1, length // 2) + self.helper(nums1, 0, length1-1, nums2, 0, length2-1, length // 2 - 1)) * 0.5
        
    def helper(self, n1, s1, e1, n2, s2, e2, k):
        len1 = e1-s1+1
        len2 = e2-s2+1
        if len1==0:
            return n2[s2+k]
        if len2==0:
            return n1[s1+k]
        if k == 0:
            return min(n1[s1], n2[s2])
        
        ind1 = len1 *k /(len1+len2)
        ind2 = k - ind1 - 1
        if n1[s1+ind1] >= n2[s2+ind2]:
            s2 += ind2+1
            e1 = s1+ind1
            k -= ind2+1
        else:
            s1 += ind1+1
            e2 = s2+ind2
            k -= ind1+1
        return self.helper(n1,s1,e1,n2,s2,e2,k)
        