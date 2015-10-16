# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        if not root: return True
        if not root.left and not root.right: return True
        inorder = []
        self.helper(root, inorder)
        k = inorder[0]
        for i in range(1,len(inorder)):
            if inorder[i] <= k:
                return False
            else:
                k = inorder[i]
        return True
        
    def helper(self,node,inorder):
        if not node: return
        self.helper(node.left,inorder)
        inorder.append(node.val)
        self.helper(node.right,inorder)
    