# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        i = j = 0
        s = []
        root = TreeNode(preorder[0])
        cur = root
        while i < len(preorder)-1:
            if preorder[i] != inorder[j]:
                i += 1
                cur.left = TreeNode(preorder[i])
                s.append(cur)
                cur = cur.left
            else:
                j += 1
                while s and s[-1].val == inorder[j]:
                    cur = s.pop(-1)
                    j += 1
                i += 1
                cur.right = TreeNode(preorder[i])
                cur = cur.right
        return root
        