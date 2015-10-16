# Definition for a  binary tree node# class TreeNode:#     def __init__(self, x):#         self.val = x#         self.left = None#         self.right = Noneclass Solution:    # @param root, a tree node    # @return an integer    def maxPathSum(self, root):        if not root: return 0        res = []        self.helper(root,res)        return max(res)    def helper(self,root,res):        l = 0        r = 0        if root.left: l = max(self.helper(root.left,res),0)        if root.right: r = max(self.helper(root.right,res),0)        res += [l+r+root.val]        return max(max(l,r) + root.val,0)        