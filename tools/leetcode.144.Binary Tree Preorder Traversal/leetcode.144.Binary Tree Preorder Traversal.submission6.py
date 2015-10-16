# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if not root: return []
        val = []
        self.helper(root,val)
        return val
    
    def helper(self, node, val):
        if not node: return
        val.append(node.val)
        self.helper(node.left, val)
        self.helper(node.right, val)