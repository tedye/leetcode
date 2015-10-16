# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root: return False
        if not root.right and not root.left:
            return sum == root.val
        r = False
        l = False
        if root.right:
            r = self.hasPathSum(root.right,sum-root.val)
        if root.left:
            l = self.hasPathSum(root.left,sum-root.val)
        return r or l
        