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
        if not root: return
        if not root.left and not root.right: return 
        
        head = root
        while head:
            next = None
            temp = TreeLinkNode(-1)
            while head:
                if head.left:
                    if not next:
                        next = head.left
                    temp.next = head.left
                    temp = temp.next
                if head.right:
                    if not next:
                        next = head.right
                    temp.next = head.right
                    temp = temp.next
                head = head.next
            head = next
        