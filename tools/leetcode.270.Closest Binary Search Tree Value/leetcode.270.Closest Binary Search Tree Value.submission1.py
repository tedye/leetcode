# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        # basically in-order travesal and find the closest
        dist = []
        result = root.val
        path = [root]
        while path:
            cur = path[-1]
            if cur:
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    heapq.heappush(dist,(abs(cur.val - target), cur.val))
                    path.append(cur.right)
        return heapq.heappop(dist)[1]
        