# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path = []
        cur = []
        self.helper(root, p, q, path, cur)
        result = None
        for i in range(len(path[0])):
            if path[0][i] == path[1][i]:
                result = path[0][i]
            else:
                break
        return result
    def helper(self, root, q,p, path, cur):
        if not root:
            return
        cur.append(root)
        if root == q:
            path.append(cur[:])
        if root == p:
            path.append(cur[:])
        self.helper(root.left,q,p,path,cur)
        self.helper(root.right,q,p, path,cur)
        cur.pop(-1)