# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1: return head
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        count = length // k
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while count > 0:
            count -= 1
            p = self.reverseKgroup(p,k)
        return dummy.next
    
    def reverseKgroup(self, p, k):
        wkset = [p.next,p.next.next,p.next.next.next]
        tail = p.next
        while k > 1:
            k -= 1
            wkset[1].next = wkset[0]
            wkset[0] = wkset[1]
            wkset[1] = wkset[2]
            if wkset[2]:
                wkset[2] = wkset[2].next
        p.next = wkset[0]
        tail.next = wkset[1]
        return tail     