# Definition for a  binary tree node# class TreeNode:#     def __init__(self, x):#         self.val = x#         self.left = None#         self.right = Noneclass Solution:    # @param root, a tree node    # @return an integer    def minDepth(self, root):        if root == None: return 0        if root.right == root.left == None: return 1        l = 0x7ffffff        if root.left != None:            l = self.minDepth(root.left)        r = 0x7ffffff        if root.right != None:            r = self.minDepth(root.right)        return 1 + min(l,r)