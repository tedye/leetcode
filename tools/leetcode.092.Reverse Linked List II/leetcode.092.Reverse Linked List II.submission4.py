# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head: return None
        if m == n: return head
        
        dummyHead = ListNode(-0x7fffffff)
        dummyHead.next = head
        
        t1 = dummyHead
        i = 0
        while i < m - 1:
            t1 = t1.next
            i += 1
        
        t2 = t1
        i = 0
        while i < n - m + 1:
            t2 = t2.next
            i += 1
        tail = t1.next
        l1 = tail
        l2 = l1.next
        l3 = l2.next
            
        while l2 != t2:
            l2.next = l1
            l1 = l2
            l2 = l3
            l3 = l3.next
        l2.next = l1
        tail.next = l3
        t1.next = l2
        
        return dummyHead.next
        