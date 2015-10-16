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
        
        lvl = [root]
        while lvl:
            for i in range(len(lvl)-1):
                lvl[i].next = lvl[i+1]
            lvl[-1].next = None
            
            next_lvl = []
            for i in lvl:
                if i.left:
                    next_lvl.append(i.left)
                if i.right:
                    next_lvl.append(i.right)
            lvl = next_lvl
        