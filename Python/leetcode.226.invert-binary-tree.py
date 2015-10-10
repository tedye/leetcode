# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        cur = [root]
        while cur:
            next = []
            for n in cur:
                temp = n.left
                n.left = n.right
                n.right = temp
                if n.right:
                    next.append(n.right)
                if n.left:
                    next.append(n.left)
            cur = next
            
        return root