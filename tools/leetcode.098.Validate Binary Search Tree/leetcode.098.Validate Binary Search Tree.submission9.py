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
        # attempt two - iterative
        if not root: return True
        if not root.right and not root.left: return True
        
        path = [root]
        visited = [False]
        val = []
        while path:
            cur = path[-1]
            if cur:
                if not visited[-1]:
                    path.append(cur.left)
                    visited.append(False)
                else:
                    val.append(cur.val)
                    path.pop(-1)
                    visited.pop(-1)
                    path.append(cur.right)
                    visited.append(False)
            else:
                path.pop(-1)
                visited.pop(-1)
                if path:
                    visited[-1] = True
        
        pos = 1
        length = len(val)
        while pos < length:
            if val[pos-1] < val[pos]:
                pos += 1
            else:
                return False
        return True
        