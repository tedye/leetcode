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
        path = [root]
        inorder = []
        while path:
            cur = path[-1]
            if cur:
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    if inorder and inorder[-1] >=cur.val:
                        return False
                    else:
                        inorder.append(cur.val)
                    path.append(cur.right)
        return True
        