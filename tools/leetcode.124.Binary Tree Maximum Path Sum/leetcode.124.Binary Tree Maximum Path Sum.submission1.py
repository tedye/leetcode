# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.res = -0x7fffffff
    def maxPathSum(self, root):
        self.res = -0x7fffffff
        if not root: return 0
        self.helper(root)
        return self.res

    def helper(self,root):
        l = 0
        r = 0
        if root.left: l = self.helper(root.left)
        if root.right: r = self.helper(root.right)
        self.res = max(l+r+root.val,self.res)
        return max(max(l,r) + root.val,0)
        