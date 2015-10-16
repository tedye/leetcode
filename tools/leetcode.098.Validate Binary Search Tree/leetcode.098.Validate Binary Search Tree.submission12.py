# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        cur = []
        return self.helper(root,cur)

    def helper(self, root, cur):
        if not root:
            return True

        l = self.helper(root.left,cur)
        valid = False
        if not cur:
            cur.append(root.val)
            valid = True
        elif root.val > cur[0]:
            valid = True
            cur[0] = root.val
        r = self.helper(root.right,cur)

        return l and valid and r
        