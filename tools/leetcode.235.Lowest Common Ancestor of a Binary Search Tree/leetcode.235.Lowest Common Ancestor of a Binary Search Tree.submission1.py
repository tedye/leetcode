# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        path = [root]
        large = max(q.val, p.val)
        small = min(q.val, p.val)
        
        while path:
            cur = path[-1]
            if cur:
                if large >= cur.val >= small:
                    return cur
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    path.append(cur.right)
        
            
        