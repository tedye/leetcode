# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n: return head
        dummy = ListNode(0)
        dummy.next = head
        i = 0
        p = dummy
        while i < m -1:
            p = p.next
            i += 1
        i = 0
        t = dummy
        while i < n:
            t = t.next
            i += 1
        tail = t.next
        t.next = None
            
        l = n - m +1
        wkset = [tail, p.next,p.next.next]
        for i in range(l):
            wkset[1].next = wkset[0]
            wkset[0] = wkset[1]
            wkset[1] = wkset[2]
            if wkset[2]:
                wkset[2] = wkset[2].next
            else:
                break
        
        p.next = wkset[0]
        return dummy.next