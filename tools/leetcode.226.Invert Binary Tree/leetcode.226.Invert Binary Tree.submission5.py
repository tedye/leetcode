# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        # basically BFS and interchange the right and left node
        if not root:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
        