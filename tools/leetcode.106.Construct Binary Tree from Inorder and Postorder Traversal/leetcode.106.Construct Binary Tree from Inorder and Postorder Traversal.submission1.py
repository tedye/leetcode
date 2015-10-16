# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        
        l = len(inorder)
        root = TreeNode(postorder[-1])
        i = j = l-1
        path = []
        cur = root
        while i > 0:
            if postorder[i] != inorder[j]:
                i -= 1
                cur.right = TreeNode(postorder[i])
                path.append(cur)
                cur = cur.right
            else:
                j -= 1
                while path and path[-1].val == inorder[j]:
                    cur = path.pop(-1)
                    j -= 1
                i -= 1
                cur.left = TreeNode(postorder[i])
                cur = cur.left
        return root
        