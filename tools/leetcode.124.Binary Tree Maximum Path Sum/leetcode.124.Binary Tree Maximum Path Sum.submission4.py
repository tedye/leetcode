# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        if not root: return 0
        return  self.helper(root)[0]
        
    def helper(self,node):
        if not node.left and not node.right:
            return [node.val,node.val]
        if node.left and not node.right:
            [a,lm] = self.helper(node.left)
            return [max(a,node.val,lm+node.val),max(node.val, node.val+lm)]
        if node.right and not node.left:
            [b,rm] = self.helper(node.right)
            return [max(b,node.val,rm+node.val),max(node.val, node.val+rm)]
        [a,lm] = self.helper(node.left)
        [b,rm] = self.helper(node.right)
        localmax = max(a,b,max(lm,rm,rm+lm)+node.val,node.val)
        pathmax = max(max(lm,rm) + node.val,node.val)
        return [localmax,pathmax]
        