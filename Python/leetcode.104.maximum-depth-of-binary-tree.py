# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)
    
    def helper(self, node):
        if not node:
            return 0
        return max(self.helper(node.left), self.helper(node.right)) +  1