# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        # attempt two - iterative
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        count = 0
        path = [root]
        visited = [False]
        m = 0x7fffffff
        while path:
            visited[-1] = True
            count += 1
            cur = path[-1]
            if cur.right:
                path.append(cur.right)
                visited.append(False)
            if cur.left:
                path.append(cur.left)
                visited.append(False)
            if not cur.left and not cur.right:
                if count < m:
                    m = count
                while visited and visited[-1]:
                    count -= 1
                    visited.pop(-1)
                    path.pop(-1)
        return m
        