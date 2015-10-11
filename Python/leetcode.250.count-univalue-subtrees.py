# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count = [0]
        self.helper(root, count)
        return count[0]
    
    def helper(self,node, count):
        if not node.left and not node.right:
            count[0] += 1
            return [True, node.val]
        
        left = [True, None]
        right = [True, None]
        if node.left:
            left = self.helper(node.left, count)
        if node.right:
            right = self.helper(node.right, count)
        if left[0] and (node.val == left[1] or left[1] == None) and right[0] and (node.val == right[1] or right[1] == None):
            count[0] += 1
            return [True, node.val]
        else:
            return [False, None]
