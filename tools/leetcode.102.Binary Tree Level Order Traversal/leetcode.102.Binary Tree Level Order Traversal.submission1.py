# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        cur = [root]
        
        while cur:
            next = []
            res.append([c.val for c in cur])
            for c in cur:
                if c.left:
                    next.append(c.left)
                if c.right:
                    next.append(c.right)
            cur = next
        return res
        