# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if not head: return None
        
        dummyLess = ListNode(-0x7fffffff)
        dummyGOrE = ListNode(-0x7fffffff)
        
        t = head
        t1 = dummyLess
        t2 = dummyGOrE
        while t != None:
            if t.val < x:
                t1.next = t
                t1 = t1.next
            else:
                t2.next = t
                t2 = t2.next
            t = t.next
        t2.next = None
        t1.next = dummyGOrE.next
        
        return dummyLess.next