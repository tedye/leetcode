# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        curlvl = [root]
        res = []
        count = 1
        while curlvl:
            if count & 1:
                res.append([c.val for c in curlvl])
            else:
                res.append([c.val for c in curlvl][::-1])
            count += 1
            next = []
            for c in curlvl:
                if c.left:
                    next.append(c.left)
                if c.right:
                    next.append(c.right)
            curlvl = next
        return res