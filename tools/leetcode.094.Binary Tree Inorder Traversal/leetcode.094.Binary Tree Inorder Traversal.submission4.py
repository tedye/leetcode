# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root: return []
        res = []
        self.helper(root,res)
        return res
    
    def helper(self,node,res):
        if not node:
            return
        
        self.helper(node.left,res)
        res.append(node.val)
        self.helper(node.right,res)
        