# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[0]
        
    def helper(self,node):
        if not node:
            return [True,0]
            
        l = self.helper(node.left)
        if not l[0]:
            return [False,None]
        r = self.helper(node.right)
        if not r[0]:
            return [False,None]
        
        if abs(r[1] - l[1]) > 1:
            return [False, None]
        else:
            return [True, max(l[1],r[1])+1]