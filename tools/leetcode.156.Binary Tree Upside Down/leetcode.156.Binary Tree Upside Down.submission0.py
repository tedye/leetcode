# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        leftbone = [root]
        rightbone = []
        temp = root
        while temp.left:
            leftbone.append(temp.left)
            rightbone.append(self.upsideDownBinaryTree(temp.right))
            temp = temp.left
        leftbone[0].left = None
        leftbone[0].right = None
        for i in range(len(rightbone)):
            leftbone[-i-1].left = rightbone[-i-1]
            leftbone[-i-1].right = leftbone[-i-2]
        return leftbone[-1]
        