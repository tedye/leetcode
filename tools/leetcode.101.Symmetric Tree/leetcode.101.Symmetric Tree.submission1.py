# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        # if symmetric inorder symmetric
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self,p, q):
        if not q and not p:
            return True
        if not q and p or not p and q:
            return False
        
        return p.val == q.val and self.helper(p.left, q.right) and self.helper(p.right, q.left)