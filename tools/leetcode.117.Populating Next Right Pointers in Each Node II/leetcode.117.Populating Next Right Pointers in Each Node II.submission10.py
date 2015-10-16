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
        
        lvl = [root]
        while lvl:
            for i in range(len(lvl)-1):
                lvl[i].next = lvl[i+1]
            next = []
            for n in lvl:
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            lvl = next
        