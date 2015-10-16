# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if not root: return
        if not root.right and not root.left: return
        
        dummy = TreeNode(0)
        temp = dummy
        rights = [root]
        while rights:
            cur = rights.pop(-1)
            while cur:
                if cur.right:
                    rights.append(cur.right)
                temp.right = cur
                cur = cur.left
                temp = temp.right
                temp.left = None
                
