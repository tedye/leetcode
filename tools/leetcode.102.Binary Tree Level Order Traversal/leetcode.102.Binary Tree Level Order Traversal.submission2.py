# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root: return []
        if not root.right and not root.left:
            return [[root.val]]
        
        d = {}
        path = [root]
        visited = [False]
        depth = 0
        while path:
            cur = path[-1]
            visited[-1] = True
            if cur.right:
                path.append(cur.right)
                visited.append(False)
            if cur.left:
                path.append(cur.left)
                visited.append(False)
            if not cur.left and not cur.right:
                while visited and visited[-1]:
                    v = path.pop(-1).val
                    visited.pop(-1)
                    if depth in d:
                        d[depth] += [v]
                    else:
                        d[depth] = [v]
                    depth -= 1
            depth += 1  
        i = 0
        res = []
        while i in d:
            res.append(d[i])
            i += 1
        return res
        