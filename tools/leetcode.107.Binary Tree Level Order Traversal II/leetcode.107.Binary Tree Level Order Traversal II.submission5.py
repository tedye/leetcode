# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if not root: return []
        if not root.right and not root.left:
            return [[root.val]]
        d = {}
        res = []
        path = [root]
        visited = [False]
        levels = [0]
        while path:
            cur = path[-1]
            level = levels[-1]
            visited[-1] = True
            if cur.right:
                path.append(cur.right)
                visited.append(False)
                levels.append(level+1)
            if cur.left:
                path.append(cur.left)
                visited.append(False)
                levels.append(level+1)
            if not cur.left and not cur.right:
                while visited and visited[-1]:
                    cur = path.pop(-1)
                    lvl = levels.pop(-1)
                    visited.pop(-1)
                    if lvl in d:
                        d[lvl].append(cur.val)
                    else:
                        d[lvl] = [cur.val]
        i = 0
        while i in d:
            res.append(d[i])
            i += 1
        return res[::-1]
                