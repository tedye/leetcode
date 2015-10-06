# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        temp = p.next
        while temp and temp.next:
            n = temp.next.next
            p.next = temp.next
            p.next.next = temp
            temp.next = n
            p = temp
            temp = n
        return dummy.next