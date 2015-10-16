# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        # attempt one - recursive
        if not root: return True
        if not root.right and not root.left:
            return True
        if self.helper(root) == -1:
            return False
        return True
    
    def helper(self, node):
        # return height if balanced, or -1
        if not node.right and not node.left:
            # at leaf level
            return 1
        if node.right and not node.left:
            if node.right.right or node.right.left:
                # inbalanced
                return -1
            else:
                return 2
        if node.left and not node.right:
            if node.left.left or node.left.right:
                return -1
            else:
                return 2
        
        l = self.helper(node.left)
        if l == -1:
            return -1
        r = self.helper(node.right)
        if r == -1:
            return -1
        if abs(l-r) > 1:
            return -1
        return 1+max(l,r)
        