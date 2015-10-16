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
        for i in leftbone:
            i.left = None
            i.right = None
        leftbone = leftbone[::-1]
        rightbone = rightbone[::-1]
        for i in range(len(rightbone)):
            leftbone[i].left = rightbone[i]
            leftbone[i].right = leftbone[i+1]
        return leftbone[0]
        