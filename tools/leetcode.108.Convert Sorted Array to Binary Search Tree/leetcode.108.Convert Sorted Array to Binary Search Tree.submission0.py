# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        l = len(nums)
        base = 1
        while base < l+1:
            base *= 2
        nums2 = []
        nums1 = [TreeNode(n) for n in nums]
        for i in range(base - l - 1):
            nums2.append(None)
            nums2.append(nums1.pop(0))
        nums2.extend(nums1)

        while len(nums2) > 1:
            next = []
            for i in range(1,len(nums2),2):
                next.append(nums2[i])
                next[-1].left = nums2[i-1]
                next[-1].right = nums2[i+1]
            nums2 = next
        return nums2[0]