class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if (m+n) & 1:
            return 1.0*self.helper(nums1,0,m-1,nums2,0,n-1,(m+n)//2)
        else:
            return 0.5*(self.helper(nums1,0,m-1,nums2,0,n-1,(m+n)//2)+self.helper(nums1,0,m-1,nums2,0,n-1,(m+n)//2-1))
            
    def helper(self,n1, s1, e1, n2, s2, e2, k):
        len1 = e1-s1+1
        len2 = e2-s2+1
        
        if len1 == 0: return n2[s2+k]
        if len2 == 0: return n1[s1+k]
        
        if k == 0: return min(n1[s1], n2[s2])
            
        t1 = (len1*k)//(len1+len2)
        t2 = k-t1-1
        
        if n1[t1+s1] > n2[t2+s2]:
            e1 = t1+s1
            s2 = t2+s2+1
            k -= t2+1
        else:
            e2 = t2+s2
            s1 = t1+s1+1
            k -= t1+1
        return self.helper(n1,s1,e1,n2,s2,e2,k)
        