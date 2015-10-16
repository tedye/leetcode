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
        res = []
        if not root:
            return res
        
        path = [root]
        while path:
            cur = path[-1]
            if cur:
                res.append(cur.val)
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    path.append(cur.right)
        return res
        