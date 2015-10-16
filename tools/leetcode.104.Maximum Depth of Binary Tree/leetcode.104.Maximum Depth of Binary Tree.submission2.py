# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root: return 0
        if not root.right and not root.left:
            return 1
        
        path = [root]
        visited = [False]
        mdepth = 1
        m = 0
        while path:
            cur = path[-1]
            visited[-1] = True
            if cur.left:
                path.append(cur.left)
                visited.append(False)
            if cur.right:
                path.append(cur.right)
                visited.append(cur.right)
            if not cur.right and not cur.left:
                if m < mdepth:
                    m = mdepth
                while visited and visited[-1]:
                    path.pop(-1)
                    visited.pop(-1)
                    mdepth -= 1
            mdepth += 1
        return m
                    
                    