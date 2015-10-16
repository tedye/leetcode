# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        cur = [0]
        res = [0]
        self.helper(root, cur, res)
        return res[0]
        
            
    def helper(self, node, cur, res):
        if not node.right and not node.left:
            res[0] += cur[0] * 10 + node.val
            return
        cur[0] = cur[0] * 10 + node.val
        if node.left:
            self.helper(node.left, cur, res)
        if node.right:
            self.helper(node.right, cur, res)
        cur[0] //= 10