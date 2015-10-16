# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
    
        head = root
        while head:
            dummy = TreeLinkNode(0)
            temp = dummy
            while head:
                if head.left:
                    dummy.next = head.left
                    dummy = dummy.next
                if head.right:
                    dummy.next = head.right
                    dummy = dummy.next
                head = head.next
            head = temp.next
            