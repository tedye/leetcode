# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # use Inorder travesal + heapq
        heap = []
        path = [root]
        while path:
            cur = path[-1]
            if cur:
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    heapq.heappush(heap,(abs(cur.val * 1.0 - target), cur.val))
                    path.append(cur.right)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        