# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if not root:
            return []
        s = []
        cur = root
        val = []
        while s or cur:
            if cur:
                val.append(cur.val)
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop(-1).right
        return val
        