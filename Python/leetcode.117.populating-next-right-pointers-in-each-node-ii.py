# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
    
        head = root
        temp = TreeLinkNode(0)
        while head:
            temp.next = None
            dummy = temp
            while head:
                if head.left:
                    dummy.next = head.left
                    dummy = dummy.next
                if head.right:
                    dummy.next = head.right
                    dummy = dummy.next
                head = head.next
            head = temp.next