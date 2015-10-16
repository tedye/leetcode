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
        if len(preorder)== 1:
            return TreeNode(preorder[0])
        
        i = j = 0
        s = []
        parent = TreeNode(preorder[0])
        cur = parent
        while i < len(preorder)-1:
            if preorder[i] == inorder[j]:
                j += 1
                while s and s[-1].val == inorder[j]:
                    cur = s.pop(-1)
                    j += 1
                i += 1
                cur.right = TreeNode(preorder[i])
                cur = cur.right
            else:
                i += 1
                cur.left = TreeNode(preorder[i])
                s.append(cur)
                cur = cur.left
        return parent
        