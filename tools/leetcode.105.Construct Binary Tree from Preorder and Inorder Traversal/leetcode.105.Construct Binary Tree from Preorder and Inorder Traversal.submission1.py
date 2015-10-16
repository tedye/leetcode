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
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        path = []
        i = j = 0
        l = len(preorder)
        current = root
        while i < l - 1:
            if preorder[i] != inorder[j]:
                i += 1
                current.left = TreeNode(preorder[i])
                path.append(current)
                current = current.left
            else:
                j += 1
                while path and path[-1].val == inorder[j]:
                    current = path.pop(-1)
                    j += 1
                i += 1
                current.right = TreeNode(preorder[i])
                current = current.right
        return root
        