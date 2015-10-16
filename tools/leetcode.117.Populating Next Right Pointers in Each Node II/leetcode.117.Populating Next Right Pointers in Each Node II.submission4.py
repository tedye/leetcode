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
            next = None
            dummy = TreeLinkNode(0)
            while head:
                if head.left:
                    if not next:
                        next = head.left
                    dummy.next = head.left
                    dummy = dummy.next
                if head.right:
                    if not next:
                        next = head.right
                    dummy.next = head.right
                    dummy = dummy.next
                head = head.next
            head = next
            