# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        # attempt one - recursive
        if not root: return True
        if not root.right and not root.left:
            return True
        if not root.right and root.left or not root.left and root.right:
            return False
        
        
        lpath = [root.left]
        lvisited = [False]
        rpath = [root.right]
        rvisited = [False]
        
        while lpath and rpath:
            flagl = 0
            flagr = 0
            lcur = lpath[-1]
            rcur = rpath[-1]
            lvisited[-1] = True
            rvisited[-1] = True
            if lcur.val != rcur.val:
                return False
            if lcur.right:
                lpath.append(lcur.right)
                lvisited.append(False)
                flagl = 1
            if rcur.left:
                rpath.append(rcur.left)
                rvisited.append(False)
                flagr = 1
            if lcur.left:
                lpath.append(lcur.left)
                lvisited.append(False)
                flagl = 2
            if rcur.right:
                rpath.append(rcur.right)
                rvisited.append(False)
                flagr = 2
            if not lcur.right and not lcur.left:
                while lvisited and lvisited[-1]:
                    lpath.pop(-1)
                    lvisited.pop(-1)
            if not rcur.right and not rcur.left:
                while rvisited and rvisited[-1]:
                    rpath.pop(-1)
                    rvisited.pop(-1)
            if flagl != flagr:
                return False
        if lpath or rpath:
            return False
        return True
        