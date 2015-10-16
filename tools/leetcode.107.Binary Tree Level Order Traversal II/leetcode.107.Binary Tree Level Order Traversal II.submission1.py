# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
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