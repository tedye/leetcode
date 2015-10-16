# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        # attempt 2 - iterative approach
        if not root:
            return False
        s = 0
        path = [root]
        visited = [False]
        while path:
            cur = path[-1]
            visited[-1] = True
            s += cur.val
            if cur.right:
                path.append(cur.right)
                visited.append(False)
            if cur.left:
                path.append(cur.left)
                visited.append(False)
            if not cur.right and not cur.left:
                # at leaf level
                if sum == s:
                    return True
                else:
                    while visited and visited[-1]:
                        visited.pop(-1)
                        s -= path.pop(-1).val

        return False
        
        