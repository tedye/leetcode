# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if not q and not p: return True
        if not q and p or not p and q: return False
        
        pathp = [p]
        pathq = [q]
        visitedp = [False]
        visitedq = [False]
        
        while pathp and pathq:
            curp = pathp[-1]
            curq = pathq[-1]
            visitedp[-1] = True
            visitedq[-1] = True
            flagp = 0
            flagq = 0
            if curp.val != curq.val:
                return False
            
            if curp.right:
                pathp.append(curp.right)
                visitedp.append(False)
                flagp = 1
            if curq.right:
                pathq.append(curq.right)
                visitedq.append(False)
                flagq = 1
            if curp.left:
                pathp.append(curp.left)
                visitedp.append(False)
                flagp = 2
            if curq.left:
                pathq.append(curq.left)
                visitedq.append(False)
                flagq = 2
            if not curq.left and not curq.right:
                while visitedq and visitedq[-1]:
                    pathq.pop(-1)
                    visitedq.pop(-1)
            if not curp.left and not curp.right:
                while visitedp and visitedp[-1]:
                    pathp.pop(-1)
                    visitedp.pop(-1)
            if flagp != flagq:
                return False
        if pathp or pathq:
            return False
        return True
                
                