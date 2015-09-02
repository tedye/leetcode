class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1+l2
        if l & 1:
            return 1.0 * self.getKth(nums1, 0, l1-1, nums2, 0, l2-1, l//2)
        else:
            return 0.5 * (self.getKth(nums1, 0, l1-1, nums2, 0, l2-1, l//2)+self.getKth(nums1, 0, l1-1, nums2, 0, l2-1, l//2 - 1))
    
    def getKth(self, n1, s1, e1, n2, s2, e2, k):
        l1 = e1 - s1 + 1
        l2 = e2 - s2 + 1
        if l1 == 0:
            return n2[s2+k]
        if l2 == 0:
            return n1[s1+k]
        if k == 0:
            return min(n1[s1], n2[s2])
        
        ind1 = (l1 * k) // (l1+l2)
        ind2 = k - ind1 - 1
        if n1[s1+ind1] < n2[s2+ind2]:
            s1 += ind1 + 1
            e2 = s2 + ind2
            k -= ind1 + 1
        else:
            s2 += ind2 + 1
            e1 = s1 + ind1
            k -= ind2 + 1
        return self.getKth(n1, s1, e1, n2, s2, e2, k)
        