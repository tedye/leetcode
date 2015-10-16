# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root == None: return
        rightBranches = [root]
        dummyTree = TreeNode(0)
        temp = dummyTree
        while rightBranches:
            cur = rightBranches.pop(-1)
            while cur:
                if cur.right:
                    rightBranches.append(cur.right)
                temp.right = cur
                temp.left = None
                cur = cur.left
                temp = temp.right
        temp.right = None
        