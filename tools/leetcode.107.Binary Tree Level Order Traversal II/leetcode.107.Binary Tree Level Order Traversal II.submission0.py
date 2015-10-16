# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        
        cur = [root]
        while cur:
            next = []
            res = [[c.val for c in cur]] +  res
            for c in cur:
                if c.left:
                    next.append(c.left)
                if c.right:
                    next.append(c.right)
            cur = next
        return res