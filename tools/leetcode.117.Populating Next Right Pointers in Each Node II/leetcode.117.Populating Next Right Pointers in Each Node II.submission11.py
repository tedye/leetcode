# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root: return 
        queue = [root]
        while queue:
            nextLayer = []
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
                if queue[i].left: nextLayer += [queue[i].left]
                if queue[i].right: nextLayer += [queue[i].right]
            queue[-1].next = None
            if queue[-1].left: nextLayer += [queue[-1].left]
            if queue[-1].right: nextLayer += [queue[-1].right]
            queue = nextLayer