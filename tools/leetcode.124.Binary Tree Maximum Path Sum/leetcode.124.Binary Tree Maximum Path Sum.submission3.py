# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if not root: return 0
        res = [-0x7fffffff]
        self.helper(root,res)
        return res[0]

    def helper(self,root,res):
        l = 0
        r = 0
        if root.left: l = self.helper(root.left,res)
        if root.right: r = self.helper(root.right,res)
        res[0] = max(l+r+root.val,res[0])
        return max(max(l,r) + root.val,0)
        