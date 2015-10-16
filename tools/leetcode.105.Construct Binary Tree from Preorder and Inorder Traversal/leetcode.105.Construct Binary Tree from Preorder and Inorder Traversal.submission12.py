# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not preorder: return None
        
        if len(preorder) == 1: return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        cut = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:cut+1],inorder[:cut])
        root.right = self.buildTree(preorder[cut+1:],inorder[cut+1:])
        return root