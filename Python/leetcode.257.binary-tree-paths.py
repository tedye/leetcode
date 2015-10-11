# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # basically DFS with path recorder
        if not root:
            return []
        result = []
        cur = []
        
        self.helper(root, result, cur)
        return result
    
    def helper(self, node, result, cur):
        if not node.left and not node.right:
            cur += node,
            result.append('->'.join([str(i.val) for i in cur]))
            cur.pop(-1)
            return
        
        cur.append(node)
        if node.left:
            self.helper(node.left, result, cur)
        if node.right:
            self.helper(node.right, result,cur)
        cur.pop(-1)
            