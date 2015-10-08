# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        length = 0
        temp = head
        nums1 = []
        while temp:
            nums1.append(TreeNode(temp.val))
            temp = temp.next
            length += 1
        base = 1
        while base < length + 1:
            base *= 2
        nums2 = []
        for i in range(base - length - 1):
            nums2.append(None)
            nums2.append(nums1.pop(0))
        nums2.extend(nums1)
        
        while len(nums2) > 1:
            next = []
            for i in range(1, len(nums2), 2):
                next.append(nums2[i])
                next[-1].left = nums2[i-1]
                next[-1].right= nums2[i+1]
            nums2 = next
        return nums2[0]