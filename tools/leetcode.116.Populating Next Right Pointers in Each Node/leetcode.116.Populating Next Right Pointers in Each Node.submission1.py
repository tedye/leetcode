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
        next = root
        wkset = [root,None]
        oldNext = None
        while wkset[0]:
            oldNext = wkset[0]
            wkset[0] = None
            while oldNext and wkset[0] == None:
                if oldNext.left:
                    wkset[0] = oldNext.left
                    wkset[1] = wkset[0]
                    if oldNext.right:
                        wkset[1].next = oldNext.right
                        wkset[1] = wkset[1].next
                elif oldNext.right:
                    wkset[0] = oldNext.right
                    wkset[1] = wkset[0]
                oldNext = oldNext.next
            while oldNext:
                if oldNext.left:
                    wkset[1].next = oldNext.left
                    wkset[1] = wkset[1].next
                if oldNext.right:
                    wkset[1].next = oldNext.right
                    wkset[1] = wkset[1].next
                oldNext = oldNext.next
        
            
                
                
                