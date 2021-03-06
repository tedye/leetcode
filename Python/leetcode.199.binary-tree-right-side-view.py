# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        cur = [root]
        
        while cur:
            res.append(cur[-1].val)
            n = []
            for c in cur:
                if c.left:
                    n.append(c.left)
                if c.right:
                    n.append(c.right)
            cur = n
        return res