# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(i.val, i) for i in lists if i]
        import heapq
        heapq.heapify(heap)
        dummy = ListNode(0)
        temp = dummy
        while heap:
            cur = heapq.heappop(heap)[1]
            temp.next = cur
            if cur.next:
                heapq.heappush(heap,(cur.next.val, cur.next))
            temp = temp.next
            temp.next = None
        return dummy.next