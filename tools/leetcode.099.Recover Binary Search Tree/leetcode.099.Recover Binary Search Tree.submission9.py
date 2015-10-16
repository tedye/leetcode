# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        cur = []
        toExchange = []
        self.helper(root,cur,toExchange)
        if toExchange:
            temp = toExchange[0].val
            toExchange[0].val = toExchange[1].val
            toExchange[1].val = temp
        return root

    def helper(self,root,cur,toExchange):
        if not root:
            return
        self.helper(root.left,cur,toExchange)
        if not cur:
            cur += [[root,root.val]]
        elif not toExchange and root.val < cur[0][1]:
            toExchange += [cur[0][0]]
            toExchange += [root]
            cur[0] = [root,root.val]
        elif root.val < cur[0][1]:
            toExchange[1] = root
            return
        else:
            cur[0] = [root,root.val]
        self.helper(root.right,cur,toExchange)
        