class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1+l2) & 1:
            return self.helper(nums1, 0, l1-1, nums2, 0, l2-1, (l1+l2) // 2) * 1.0
        else:
            return 0.5 *(self.helper(nums1, 0, l1-1, nums2, 0, l2-1, (l1+l2) // 2) +  self.helper(nums1, 0, l1-1, nums2, 0, l2-1, (l1+l2) // 2 - 1))
            
    def helper(self, n1, s1, e1, n2, s2,e2, k):
        l1 = e1-s1+1
        l2 = e2-s2+1
        
        if l1 == 0:
            return n2[s2+k]
        if l2 == 0:
            return n1[s1+k]
        if k == 0:
            return min(n1[s1],n2[s2])
        
        ind1 = (k * l1) // (l1+l2)
        ind2 = k - ind1 - 1
        if n1[s1+ind1] > n2[s2+ind2]:
            s2 = s2+ind2+1
            e1 = s1+ind1
            k -= ind2+1
        else:
            s1 = s1+ind1+1
            e2 = s2+ind2
            k -= ind1+1
        return self.helper(n1, s1, e1, n2, s2,e2, k)
        
        